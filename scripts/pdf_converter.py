import os
import pdfplumber
import pandas as pd
from datetime import datetime
import re
import time
import sys
import threading

class TransactionValidator:
    """Enhanced validator for PDF transaction extraction accuracy"""
    
    def __init__(self):
        self.validation_results = {}
        self.potential_missed = []
        
    def validate_extraction(self, pdf_path, extracted_data, statement_type):
        """Main validation method that runs all checks"""
        print(f"\n🔍 VALIDATING: {os.path.basename(pdf_path)}")
        
        validation_result = {
            'pdf_file': os.path.basename(pdf_path),
            'statement_type': statement_type,
            'extracted_count': len(extracted_data),
            'potential_missed': [],
            'amount_discrepancy': None,
            'confidence_score': 0
        }
        
        # Method 1: Count potential transaction lines in raw text
        raw_count = self.count_potential_transactions_in_text(pdf_path, statement_type)
        validation_result['estimated_total'] = raw_count
        
        # Method 2: Check for amount discrepancies
        amount_check = self.validate_amounts(pdf_path, extracted_data, statement_type)
        validation_result['amount_discrepancy'] = amount_check
        
        # Method 3: Find potential missed transactions
        missed_transactions = self.find_potential_missed_transactions(pdf_path, extracted_data, statement_type)
        validation_result['potential_missed'] = missed_transactions
        
        # Method 4: Calculate confidence score
        validation_result['confidence_score'] = self.calculate_confidence_score(validation_result)
        
        # Method 5: Generate validation report
        self.print_validation_report(validation_result)
        
        return validation_result
    
    def count_potential_transactions_in_text(self, pdf_path, statement_type):
        """Count lines that look like transactions in the raw PDF text"""
        transaction_count = 0
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    try:
                        text = page.extract_text()
                        if not text:
                            continue
                            
                        lines = text.split('\n')
                        for line in lines:
                            line = line.strip()
                            
                            # Skip obvious non-transaction lines
                            if (len(line) < 10 or 
                                'Merchant Name' in line or
                                'Date of' in line or
                                'Transaction' in line or
                                'ACCOUNT ACTIVITY' in line or
                                'Page' in line or
                                'Statement' in line or
                                line.startswith('This Statement') or
                                line.startswith('CHASE') or
                                line.startswith('AMERICAN EXPRESS')):
                                continue
                            
                            # Check if line looks like a transaction
                            if statement_type == 'amex':
                                if self.looks_like_amex_transaction(line):
                                    transaction_count += 1
                            elif statement_type == 'chase':
                                if self.looks_like_chase_transaction(line):
                                    transaction_count += 1
                    except Exception:
                        continue
        except Exception as e:
            print(f"❌ Error counting transactions: {e}")
            
        return transaction_count
    
    def looks_like_amex_transaction(self, line):
        """Check if a line looks like an AmEx transaction"""
        # Pattern: Date + text + amount
        date_pattern = r'^\d{1,2}/\d{1,2}(?:/\d{2,4})?'
        amount_pattern = r'[-]?\$?[\d,]+\.\d{2}$'
        
        return (re.search(date_pattern, line) and 
                re.search(amount_pattern, line) and
                len(line.split()) >= 3)
    
    def looks_like_chase_transaction(self, line):
        """Check if a line looks like a Chase transaction"""
        # Pattern: MM/DD + text + amount
        pattern = r'^\d{1,2}/\d{1,2}\s*(&?).*\d{1,3}(?:,\d{3})*\.\d{2}$'
        return re.match(pattern, line) is not None
    
    def validate_amounts(self, pdf_path, extracted_data, statement_type):
        """Look for total amount discrepancies"""
        try:
            # Calculate sum of extracted transactions
            extracted_total = sum(float(t['Amount'].replace(',', '')) for t in extracted_data)
            
            # Look for statement totals in PDF
            statement_totals = self.find_statement_totals(pdf_path, statement_type)
            
            if statement_totals:
                for total_type, amount in statement_totals.items():
                    difference = abs(extracted_total - amount)
                    if difference > 0.01:  # Allow for small rounding differences
                        return {
                            'extracted_total': extracted_total,
                            'statement_total': amount,
                            'total_type': total_type,
                            'difference': difference
                        }
            
            return None
            
        except Exception as e:
            print(f"❌ Error validating amounts: {e}")
            return None
    
    def find_statement_totals(self, pdf_path, statement_type):
        """Extract total amounts from PDF (New Charges, etc.)"""
        totals = {}
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                full_text = ""
                for page in pdf.pages:
                    try:
                        text = page.extract_text()
                        if text:
                            full_text += text + "\n"
                    except Exception:
                        continue
                
                # Look for common total patterns
                if statement_type == 'amex':
                    # AmEx patterns
                    patterns = {
                        'new_charges': r'New Charges.*?\$?([\d,]+\.\d{2})',
                        'total_charges': r'Total.*?Charges.*?\$?([\d,]+\.\d{2})',
                        'purchases': r'Purchases.*?\$?([\d,]+\.\d{2})'
                    }
                elif statement_type == 'chase':
                    # Chase patterns
                    patterns = {
                        'purchases': r'Purchases.*?\$?([\d,]+\.\d{2})',
                        'new_charges': r'New Charges.*?\$?([\d,]+\.\d{2})',
                        'total_activity': r'Total.*?Activity.*?\$?([\d,]+\.\d{2})'
                    }
                
                for total_type, pattern in patterns.items():
                    matches = re.findall(pattern, full_text, re.IGNORECASE)
                    if matches:
                        try:
                            amount = float(matches[0].replace(',', ''))
                            totals[total_type] = amount
                        except ValueError:
                            continue
                            
        except Exception as e:
            print(f"❌ Error finding statement totals: {e}")
            
        return totals
    
    def find_potential_missed_transactions(self, pdf_path, extracted_data, statement_type):
        """Find lines that look like transactions but weren't extracted"""
        potential_missed = []
        extracted_lines = set()
        
        # Create a set of extracted transaction signatures
        for transaction in extracted_data:
            signature = f"{transaction['Date']}|{transaction['Merchant'][:20]}|{transaction['Amount']}"
            extracted_lines.add(signature)
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    try:
                        text = page.extract_text()
                        if not text:
                            continue
                            
                        lines = text.split('\n')
                        for line_num, line in enumerate(lines, 1):
                            line = line.strip()
                            
                            # Check if this looks like a transaction
                            if statement_type == 'amex' and self.looks_like_amex_transaction(line):
                                parsed = self.quick_parse_amex_line(line)
                                if parsed:
                                    signature = f"{parsed['date']}|{parsed['merchant'][:20]}|{parsed['amount']}"
                                    if signature not in extracted_lines:
                                        potential_missed.append({
                                            'page': page_num,
                                            'line': line_num,
                                            'text': line,
                                            'parsed': parsed
                                        })
                            
                            elif statement_type == 'chase' and self.looks_like_chase_transaction(line):
                                parsed = self.quick_parse_chase_line(line)
                                if parsed:
                                    signature = f"{parsed['date']}|{parsed['merchant'][:20]}|{parsed['amount']}"
                                    if signature not in extracted_lines:
                                        potential_missed.append({
                                            'page': page_num,
                                            'line': line_num,
                                            'text': line,
                                            'parsed': parsed
                                        })
                    except Exception:
                        continue
        except Exception as e:
            print(f"❌ Error finding missed transactions: {e}")
            
        return potential_missed
    
    def quick_parse_amex_line(self, line):
        """Quickly parse an AmEx line to extract basic info"""
        try:
            date_match = re.match(r'^(\d{1,2}/\d{1,2}(?:/\d{2,4})?)', line)
            amount_match = re.search(r'([-]?\$?[\d,]+\.\d{2})$', line)
            
            if date_match and amount_match:
                date_part = date_match.group(1)
                amount_str = amount_match.group(1).replace('$', '').replace(',', '')
                
                # Skip negative amounts
                try:
                    if float(amount_str) <= 0:
                        return None
                except ValueError:
                    return None
                
                # Extract merchant (simplified)
                start = date_match.end()
                end = amount_match.start()
                merchant = line[start:end].strip()
                
                return {
                    'date': date_part,
                    'merchant': merchant,
                    'amount': amount_str
                }
        except Exception:
            pass
        return None
    
    def quick_parse_chase_line(self, line):
        """Quickly parse a Chase line to extract basic info"""
        try:
            pattern = r'^(\d{1,2}/\d{1,2})\s*(&?)\s*(.+?)\s+([-]?\d{1,3}(?:,\d{3})*\.\d{2})$'
            match = re.match(pattern, line)
            
            if match:
                date = match.group(1)
                merchant = match.group(3).strip()
                amount = match.group(4)
                
                # Skip negative amounts
                try:
                    if float(amount) <= 0:
                        return None
                except ValueError:
                    return None
                
                return {
                    'date': date,
                    'merchant': merchant,
                    'amount': amount
                }
        except Exception:
            pass
        return None
    
    def calculate_confidence_score(self, validation_result):
        """Calculate a confidence score (0-100) for the extraction"""
        score = 100
        
        extracted = validation_result['extracted_count']
        estimated = validation_result['estimated_total']
        missed = len(validation_result['potential_missed'])
        
        # Penalize based on extraction ratio
        if estimated > 0:
            extraction_ratio = extracted / estimated
            if extraction_ratio < 0.95:
                score -= (1 - extraction_ratio) * 50
        
        # Penalize for potential missed transactions
        if missed > 0:
            penalty = min(missed * 5, 30)  # Max 30 point penalty
            score -= penalty
        
        # Penalize for amount discrepancies
        if validation_result['amount_discrepancy']:
            diff_percent = (validation_result['amount_discrepancy']['difference'] / 
                          validation_result['amount_discrepancy']['extracted_total']) * 100
            penalty = min(diff_percent * 2, 25)  # Max 25 point penalty
            score -= penalty
        
        return max(0, int(score))
    
    def print_validation_report(self, result):
        """Print a detailed validation report"""
        print(f"\n📊 VALIDATION REPORT for {result['pdf_file']}")
        print("=" * 60)
        
        print(f"📄 Statement Type: {result['statement_type'].upper()}")
        print(f"✅ Extracted Transactions: {result['extracted_count']}")
        print(f"🔢 Estimated Total in PDF: {result['estimated_total']}")
        
        if result['extracted_count'] != result['estimated_total']:
            diff = result['estimated_total'] - result['extracted_count']
            print(f"⚠️  Potential Missing: {diff} transactions")
        else:
            print(f"✅ Perfect match!")
        
        # Amount validation
        if result['amount_discrepancy']:
            disc = result['amount_discrepancy']
            print(f"\n💰 AMOUNT VALIDATION:")
            print(f"   Extracted Total: ${disc['extracted_total']:,.2f}")
            print(f"   Statement {disc['total_type']}: ${disc['statement_total']:,.2f}")
            print(f"   Difference: ${disc['difference']:,.2f}")
        else:
            print(f"💰 Amount Validation: ✅ No discrepancies found")
        
        # Potential missed transactions
        if result['potential_missed']:
            print(f"\n🚨 POTENTIAL MISSED TRANSACTIONS ({len(result['potential_missed'])}):")
            for i, missed in enumerate(result['potential_missed'][:5], 1):  # Show first 5
                print(f"   {i}. Page {missed['page']}: {missed['text'][:80]}...")
            
            if len(result['potential_missed']) > 5:
                print(f"   ... and {len(result['potential_missed']) - 5} more")
        else:
            print(f"🚨 Potential Missed: ✅ None found")
        
        # Confidence score
        score = result['confidence_score']
        if score >= 95:
            emoji = "🟢"
            status = "EXCELLENT"
        elif score >= 85:
            emoji = "🟡"
            status = "GOOD"
        else:
            emoji = "🔴"
            status = "NEEDS REVIEW"
        
        print(f"\n{emoji} CONFIDENCE SCORE: {score}% ({status})")
        print("=" * 60)

class UniversalPDFToExcelConverter:
    def __init__(self):
        self.convert_folder = "Convert"
        self.excel_folder = "Excel"
        self.chase_date_range = None
        self.progress_window = None
        self.validator = TransactionValidator()
        
    def show_progress_window(self):
        """Show a clean progress window to indicate the program is running"""
        try:
            import tkinter as tk
            from tkinter import ttk
            
            self.progress_window = tk.Tk()
            self.progress_window.title("PDF to Excel Converter")
            self.progress_window.geometry("350x150")
            self.progress_window.resizable(False, False)
            
            # Center the window
            self.progress_window.eval('tk::PlaceWindow . center')
            
            # Main frame
            main_frame = tk.Frame(self.progress_window, padx=20, pady=20)
            main_frame.pack(fill=tk.BOTH, expand=True)
            
            # Title
            title_label = tk.Label(main_frame, text="🏦 PDF to Excel Converter", 
                                 font=("Arial", 14, "bold"))
            title_label.pack(pady=(0, 15))
            
            # Status label
            self.status_label = tk.Label(main_frame, text="🚀 Starting conversion process...", 
                                       font=("Arial", 10))
            self.status_label.pack(pady=(0, 15))
            
            # Progress bar
            self.progress_bar = ttk.Progressbar(main_frame, mode='indeterminate')
            self.progress_bar.pack(fill=tk.X, pady=(0, 15))
            self.progress_bar.start(10)
            
            # Current file label
            self.file_label = tk.Label(main_frame, text="", 
                                     font=("Arial", 9), fg="gray")
            self.file_label.pack()
            
            # Don't allow closing
            self.progress_window.protocol("WM_DELETE_WINDOW", lambda: None)
            
            return self.progress_window
            
        except Exception:
            return None
    
    def update_progress(self, status_text, file_text="", force_update=False):
        """Update the progress window with current status (simplified)"""
        try:
            if self.progress_window and (force_update or time.time() - getattr(self, '_last_update', 0) > 0.3):
                self.status_label.config(text=status_text)
                if file_text:
                    self.file_label.config(text=file_text)
                self.progress_window.update_idletasks()
                self._last_update = time.time()
        except Exception:
            # Fallback to console only for critical updates
            if force_update:
                print(status_text)
    
    def close_progress_window(self):
        """Close the progress window"""
        try:
            if self.progress_window:
                self.progress_bar.stop()
                self.progress_window.destroy()
                self.progress_window = None
        except Exception:
            pass
        
    def setup_folders(self):
        """Create the Convert and Excel folders if they don't exist"""
        try:
            if not os.path.exists(self.convert_folder):
                os.makedirs(self.convert_folder)
                self.update_progress("📁 Created Convert folder", f"Created '{self.convert_folder}' folder")
                
            if not os.path.exists(self.excel_folder):
                os.makedirs(self.excel_folder)
                self.update_progress("📁 Created Excel folder", f"Created '{self.excel_folder}' folder")
        except Exception as e:
            self.update_progress("⚠️ Folder creation warning", f"Could not create folders: {str(e)}")
    
    def extract_chase_date_range(self, text):
        """Extract the date range from Chase PDF ACCOUNT SUMMARY section"""
        try:
            lines = text.split('\n')
            
            for i, line in enumerate(lines):
                # Look for "Opening/Closing Date" or similar patterns
                if ('Opening/Closing Date' in line or 
                    'OPENING/CLOSING DATE' in line.upper()):
                    
                    # The date range might be on the same line or the next line
                    date_line = line
                    if i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        if re.search(r'\d{2}/\d{2}/\d{2}', next_line):
                            date_line = next_line
                    
                    # Extract date range pattern: MM/DD/YY - MM/DD/YY
                    date_pattern = r'(\d{1,2}/\d{1,2}/\d{2,4})\s*-\s*(\d{1,2}/\d{1,2}/\d{2,4})'
                    match = re.search(date_pattern, date_line)
                    
                    if match:
                        start_date = match.group(1)
                        end_date = match.group(2)
                        
                        # Convert to full format
                        start_full = self.convert_chase_date_to_full(start_date)
                        end_full = self.convert_chase_date_to_full(end_date)
                        
                        self.update_progress("📅 Found Chase date range", 
                                           f"Date range: {start_full} to {end_full}", force_update=True)
                        
                        return {
                            'start': start_full,
                            'end': end_full,
                            'start_month': int(start_full.split('/')[0]),
                            'end_month': int(end_full.split('/')[0]),
                            'start_year': int(start_full.split('/')[2]),
                            'end_year': int(end_full.split('/')[2])
                        }
            
            # Fallback: try to find any date pattern in ACCOUNT SUMMARY section
            account_summary_section = ""
            in_summary = False
            
            for line in lines:
                if 'ACCOUNT SUMMARY' in line.upper():
                    in_summary = True
                    continue
                elif in_summary and (line.strip() == "" or 
                                   'YOUR ACCOUNT MESSAGES' in line.upper() or
                                   'ACCOUNT ACTIVITY' in line.upper()):
                    break
                elif in_summary:
                    account_summary_section += line + "\n"
            
            # Look for any date range in the summary section
            date_pattern = r'(\d{1,2}/\d{1,2}/\d{2,4})\s*-\s*(\d{1,2}/\d{1,2}/\d{2,4})'
            match = re.search(date_pattern, account_summary_section)
            
            if match:
                start_date = match.group(1)
                end_date = match.group(2)
                
                start_full = self.convert_chase_date_to_full(start_date)
                end_full = self.convert_chase_date_to_full(end_date)
                
                self.update_progress("📅 Found Chase date range (fallback)", 
                                   f"Date range: {start_full} to {end_full}", force_update=True)
                
                return {
                    'start': start_full,
                    'end': end_full,
                    'start_month': int(start_full.split('/')[0]),
                    'end_month': int(end_full.split('/')[0]),
                    'start_year': int(start_full.split('/')[2]),
                    'end_year': int(end_full.split('/')[2])
                }
            
        except Exception as e:
            self.update_progress("⚠️ Date extraction warning", f"Could not extract Chase date range", force_update=True)
        
        return None
    
    def convert_chase_date_to_full(self, date_str):
        """Convert MM/DD/YY to MM/DD/YYYY"""
        try:
            parts = date_str.split('/')
            if len(parts) == 3:
                month, day, year = parts
                if len(year) == 2:
                    year_num = int(year)
                    if year_num >= 50:
                        full_year = f"19{year_num}"
                    else:
                        full_year = f"20{year_num}"
                    return f"{month}/{day}/{full_year}"
                else:
                    return date_str
        except Exception:
            pass
        return date_str
    
    def get_chase_transaction_year(self, transaction_month):
        """Determine the correct year for a Chase transaction based on the date range"""
        try:
            if not self.chase_date_range:
                # Fallback to current year
                return datetime.now().year
            
            start_month = self.chase_date_range['start_month']
            end_month = self.chase_date_range['end_month']
            start_year = self.chase_date_range['start_year']
            end_year = self.chase_date_range['end_year']
            
            # Handle year boundary cases (e.g., 12/24/24 - 01/23/25)
            if start_year != end_year:
                if transaction_month >= start_month:
                    return start_year
                else:
                    return end_year
            else:
                # Same year for all transactions
                return start_year
                
        except Exception:
            return datetime.now().year
            
    def detect_statement_type(self, text, filename):
        """Detect if the PDF is American Express or Chase"""
        try:
            text_upper = text.upper()
            filename_upper = filename.upper()
            
            # Check filename first for more reliable detection
            if 'AMEX' in filename_upper or 'AMERICAN' in filename_upper:
                return 'amex'
            elif 'CHASE' in filename_upper:
                return 'chase'
            
            # Fallback to content detection
            if 'AMERICAN EXPRESS' in text_upper or 'AMAZON BUSINESS PRIME CARD' in text_upper:
                return 'amex'
            elif 'CHASE' in text_upper and ('ULTIMATE REWARDS' in text_upper or 'ACCOUNT ACTIVITY' in text_upper):
                return 'chase'
            else:
                return 'unknown'
        except Exception:
            return 'unknown'
    
    def extract_pdf_content(self, pdf_path):
        """Extract transaction data and validate results"""
        extracted_data = []
        statement_type = 'unknown'
        
        self.update_progress("📄 Reading PDF content...", f"Processing: {os.path.basename(pdf_path)}", force_update=True)
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                # Get full text for detection and date extraction
                full_text = ""
                for page in pdf.pages:
                    try:
                        page_text = page.extract_text()
                        if page_text:
                            full_text += page_text + "\n"
                    except Exception:
                        continue
                
                filename = os.path.basename(pdf_path)
                statement_type = self.detect_statement_type(full_text, filename)
                self.update_progress(f"🔍 Detected: {statement_type}", "", force_update=True)
                
                # Extract date range for Chase statements
                if statement_type == 'chase':
                    self.chase_date_range = self.extract_chase_date_range(full_text)
                
                # Extract transactions from all pages
                self.update_progress(f"📖 Processing {len(pdf.pages)} pages...", "", force_update=True)
                
                for page_num, page in enumerate(pdf.pages, 1):
                    try:
                        page_text = page.extract_text()
                        if page_text:
                            if page_num % 5 == 1 or page_num == len(pdf.pages):
                                self.update_progress(f"📄 Processing page {page_num}...", "", force_update=True)
                            
                            if statement_type == 'amex':
                                page_transactions = self.parse_amex_page(page_text, page_num)
                            elif statement_type == 'chase':
                                page_transactions = self.parse_chase_page(page_text, page_num)
                            else:
                                continue
                            
                            extracted_data.extend(page_transactions)
                    except Exception as e:
                        continue
                
                # VALIDATION STEP - Add this after extraction
                if extracted_data and statement_type != 'unknown':
                    self.update_progress("🔍 Validating extraction...", "Checking for missed transactions", force_update=True)
                    validation_result = self.validator.validate_extraction(pdf_path, extracted_data, statement_type)
                    
                    # Store validation results for later reporting
                    self.validator.validation_results[pdf_path] = validation_result
        
        except Exception as e:
            self.update_progress("❌ PDF processing error", f"Error: {str(e)}")
            return None, statement_type
            
        return extracted_data, statement_type
    
    def create_validation_report(self):
        """Create a comprehensive validation report"""
        report_path = os.path.join(self.excel_folder, f"Validation_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        
        try:
            with open(report_path, 'w') as f:
                f.write("PDF TO EXCEL CONVERSION - VALIDATION REPORT\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                for pdf_path, result in self.validator.validation_results.items():
                    f.write(f"FILE: {result['pdf_file']}\n")
                    f.write("-" * 30 + "\n")
                    f.write(f"Statement Type: {result['statement_type'].upper()}\n")
                    f.write(f"Extracted: {result['extracted_count']} transactions\n")
                    f.write(f"Estimated Total: {result['estimated_total']} transactions\n")
                    f.write(f"Confidence Score: {result['confidence_score']}%\n")
                    
                    if result['amount_discrepancy']:
                        disc = result['amount_discrepancy']
                        f.write(f"Amount Discrepancy: ${disc['difference']:,.2f}\n")
                    
                    if result['potential_missed']:
                        f.write(f"Potential Missed: {len(result['potential_missed'])} transactions\n")
                        f.write("Details:\n")
                        for missed in result['potential_missed']:
                            f.write(f"  Page {missed['page']}: {missed['text']}\n")
                    
                    f.write("\n")
                
            print(f"\n📋 Validation report saved: {report_path}")
            
        except Exception as e:
            print(f"❌ Error creating validation report: {e}")
    
    def parse_amex_page(self, page_text, page_num):
        """Parse American Express transactions from a single page"""
        transactions = []
        
        try:
            lines = page_text.split('\n')
            
            for i, line in enumerate(lines):
                try:
                    line = line.strip()
                    
                    # Skip empty lines and headers
                    if (len(line) < 8 or
                        'Merchant Name' in line or
                        '$ Amount' in line or
                        'Date of' in line or
                        line.startswith('Transaction') or
                        line.startswith('Amazon Business') or
                        line.startswith('AMERICAN EXPRESS') or
                        line.startswith('Account Ending') or
                        line.startswith('Page') or
                        line.startswith('Customer Care')):
                        continue
                    
                    # Try to parse as transaction
                    transaction = self.parse_amex_transaction_line(line)
                    if transaction:
                        transactions.append(transaction)
                
                except Exception:
                    continue
        
        except Exception:
            pass
        
        return transactions
    
    def parse_amex_transaction_line(self, line):
        """Parse individual American Express transaction line"""
        try:
            # Step 1: Extract date (MM/DD or MM/DD/YY) from the beginning
            date_match = re.match(r'^(\d{1,2}/\d{1,2}(?:/\d{2,4})?)', line)
            if not date_match:
                return None
            
            date_part = date_match.group(1)
            remaining_text = line[date_match.end():].strip()
            
            # Step 2: Extract amount from the end (look for $XX.XX pattern)
            amount_match = re.search(r'([-]?\$?[\d,]+\.\d{2})$', remaining_text)
            if not amount_match:
                return None
            
            amount_str = amount_match.group(1)
            merchant_and_location = remaining_text[:amount_match.start()].strip()
            
            # Step 3: Clean up amount and check if it's a charge (positive)
            amount_str = amount_str.replace('$', '').replace(',', '')
            
            # Skip negative amounts (payments/credits)
            try:
                amount_value = float(amount_str)
                if amount_value <= 0:
                    return None  # Skip payments and credits
            except ValueError:
                return None  # Skip if amount can't be parsed
            
            # Step 4: Extract ONLY merchant name from the middle part
            merchant_name = self.extract_merchant_name(merchant_and_location)
            
            if not merchant_name or len(merchant_name) < 3:
                return None
            
            # Step 5: Handle date conversion
            full_date = self.convert_date(date_part)
            if not full_date:
                return None
            
            return {
                'Date': full_date,
                'Merchant': merchant_name,
                'Amount': amount_str
            }
        
        except Exception:
            return None
    
    def extract_merchant_name(self, text):
        """Extract only the merchant name, excluding location and personal info"""
        try:
            # Remove common prefixes
            text = re.sub(r'^(AplPay|TST\*|SQ \*)', '', text).strip()
            
            # Split by common delimiters and patterns
            words = text.split()
            merchant_parts = []
            
            for word in words:
                # Stop at common location indicators
                if (word.upper() in ['CA', 'NY', 'TX', 'FL', 'WA', 'OR', 'NV', 'AZ'] or  # State codes
                    re.match(r'^\d{3}-\d{3}-\d{4}$', word) or  # Phone numbers
                    re.match(r'^\d{10,}$', word) or  # Long numbers
                    word.lower().endswith('.com') or  # Websites
                    word.lower().endswith('.net') or
                    word.lower().endswith('.org') or
                    len(word) > 20):  # Very long words (likely IDs or URLs)
                    break
                
                # Add word to merchant name if it looks valid
                if (len(word) >= 2 and 
                    not word.isdigit() and 
                    word.upper() not in ['AND', 'THE', 'OF', 'IN', 'AT', 'FOR']):
                    merchant_parts.append(word)
            
            # Join the merchant parts
            merchant_name = ' '.join(merchant_parts)
            
            # Clean up common patterns
            merchant_name = re.sub(r'\s+', ' ', merchant_name)  # Multiple spaces
            merchant_name = re.sub(r'[#*]+.*$', '', merchant_name)  # Remove # and * suffixes
            merchant_name = merchant_name.strip()
            
            # Additional cleanup for specific patterns
            merchant_name = re.sub(r'\s+\d{3,}$', '', merchant_name)
            
            return merchant_name
        
        except Exception:
            return ""
    
    def convert_date(self, date_str):
        """Convert date string to full format"""
        try:
            if '/' in date_str:
                date_components = date_str.split('/')
                if len(date_components) == 3:
                    # Full date with year (MM/DD/YY)
                    month, day, year = date_components
                    if len(year) == 2:
                        # Convert 2-digit year to 4-digit year
                        year_num = int(year)
                        if year_num >= 50:  # Assume 1950-1999
                            full_year = f"19{year_num}"
                        else:  # Assume 2000-2049
                            full_year = f"20{year_num}"
                        return f"{month}/{day}/{full_year}"
                    else:
                        return date_str
                elif len(date_components) == 2:
                    # MM/DD format - use current year
                    current_year = datetime.now().year
                    return f"{date_str}/{current_year}"
        except Exception:
            pass
        
        return None
    
    def parse_chase_page(self, page_text, page_num):
        """Parse Chase transactions from a single page"""
        transactions = []
        
        try:
            lines = page_text.split('\n')
            
            for line in lines:
                try:
                    line = line.strip()
                    
                    # Skip headers and non-transaction lines
                    if (len(line) < 10 or 
                        'Date of' in line or
                        'Transaction' in line or
                        'Merchant Name' in line or
                        'ACCOUNT ACTIVITY' in line or
                        'Page' in line or
                        'Statement' in line or
                        'Customer Service' in line or
                        'www.' in line or
                        line.startswith('This Statement') or
                        line.startswith('CHASE') or
                        line.startswith('ULTIMATE REWARDS')):
                        continue
                    
                    transaction = self.parse_chase_transaction_line(line)
                    if transaction:
                        transactions.append(transaction)
                
                except Exception:
                    continue
        
        except Exception:
            pass
        
        return transactions
    
    def parse_chase_transaction_line(self, line):
        """Parse individual Chase transaction line"""
        try:
            # Chase format: MM/DD [&] MERCHANT_NAME LOCATION AMOUNT
            date_pattern = r'^(\d{1,2}/\d{1,2})\s*(&?)\s*(.+?)\s+([-]?\d{1,3}(?:,\d{3})*\.\d{2})$'
            
            match = re.match(date_pattern, line)
            if match:
                date = match.group(1)
                merchant_and_location = match.group(3).strip()
                amount = match.group(4)
                
                # Clean up merchant name
                merchant_desc = re.sub(r'\s+', ' ', merchant_and_location)
                merchant_desc = re.sub(r'\s+[A-Z]{2}$', '', merchant_desc)  # Remove state codes
                merchant_desc = re.sub(r'\s+\d{3}-\d{3}-\d{4}$', '', merchant_desc)  # Remove phone numbers
                merchant_desc = re.sub(r'\s+\d{10,}$', '', merchant_desc)  # Remove long numbers
                
                # Skip negative amounts (payments/credits)
                try:
                    amount_value = float(amount)
                    if amount_value <= 0:
                        return None  # Skip payments and credits
                except ValueError:
                    return None  # Skip if amount can't be parsed
                
                # Get the correct year based on the date range
                transaction_month = int(date.split('/')[0])
                correct_year = self.get_chase_transaction_year(transaction_month)
                full_date = f"{date}/{correct_year}"
                
                return {
                    'Date': full_date,
                    'Merchant': merchant_desc,
                    'Amount': amount
                }
        
        except Exception:
            pass
        
        return None
    
    def process_all_pdfs(self):
        """Process all PDFs and create combined Excel files with validation"""
        self.update_progress("🚀 Starting PDF processing...", "Initializing conversion process")
        start_time = time.time()
        
        try:
            self.setup_folders()
            
            # Get all PDF files
            pdf_files = []
            try:
                pdf_files = [f for f in os.listdir(self.convert_folder) if f.lower().endswith('.pdf')]
            except Exception:
                self.update_progress("❌ Could not access Convert folder", "")
                return 0, 0
            
            if not pdf_files:
                self.update_progress("❌ No PDF files found", "Add PDFs to Convert folder and try again")
                return 0, 0
            
            self.update_progress(f"📁 Found {len(pdf_files)} PDF file(s)", f"Files: {', '.join(pdf_files)}", force_update=True)
            
            # Separate data by statement type
            amex_data = []
            chase_data = []
            
            for i, pdf_file in enumerate(pdf_files, 1):
                try:
                    pdf_path = os.path.join(self.convert_folder, pdf_file)
                    self.update_progress(f"📄 Processing PDF {i}/{len(pdf_files)}", f"{pdf_file}", force_update=True)
                    
                    data, statement_type = self.extract_pdf_content(pdf_path)
                    
                    if data:
                        if statement_type == 'amex':
                            amex_data.extend(data)
                        elif statement_type == 'chase':
                            chase_data.extend(data)
                        
                        # Only update totals, not every transaction
                        self.update_progress(f"✅ Extracted {len(data)} transactions", "", force_update=True)
                    else:
                        self.update_progress(f"❌ Failed to extract data from {pdf_file}", "", force_update=True)
                
                except Exception as e:
                    self.update_progress(f"❌ Error processing {pdf_file}", f"Error: {str(e)}", force_update=True)
                    continue
            
            self.update_progress("📈 Creating Excel files...", 
                               f"AmEx: {len(amex_data)}, Chase: {len(chase_data)} transactions", force_update=True)
            
            # Create Excel files
            files_created = 0
            
            if amex_data:
                self.update_progress("📝 Creating AmEx Excel file...", "", force_update=True)
                success = self.create_excel_file(amex_data, 'AmEx_Combined')
                if success:
                    files_created += 1
            
            if chase_data:
                self.update_progress("📝 Creating Chase Excel file...", "", force_update=True)
                success = self.create_excel_file(chase_data, 'Chase_Combined')
                if success:
                    files_created += 1
            
            # Generate validation report BEFORE returning
            try:
                if hasattr(self, 'validator') and self.validator.validation_results:
                    self.update_progress("📋 Creating validation report...", "", force_update=True)
                    self.create_validation_report()
            except Exception as e:
                print(f"❌ Error creating validation report: {e}")
            
            end_time = time.time()
            processing_time = end_time - start_time
            
            total_transactions = len(amex_data) + len(chase_data)
            self.update_progress("🎉 Processing Complete!", 
                               f"Files: {files_created}, Transactions: {total_transactions}", force_update=True)
            
            return files_created, total_transactions
        
        except Exception as e:
            self.update_progress("❌ Unexpected error occurred", f"Error: {str(e)}")
            return 0, 0
    
    def create_excel_file(self, data, filename_base):
        """Create Excel file with extracted data"""
        try:
            df = pd.DataFrame(data)
            
            if df.empty:
                self.update_progress(f"❌ No data for {filename_base}", "")
                return False
            
            # Generate filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            excel_filename = f"{filename_base}_{timestamp}.xlsx"
            excel_path = os.path.join(self.excel_folder, excel_filename)
            
            try:
                with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
                    # Write data to Excel
                    df.to_excel(writer, sheet_name='Transactions', index=False)
                    
                    # Get worksheet for formatting
                    worksheet = writer.sheets['Transactions']
                    
                    # Auto-adjust column widths
                    for column in worksheet.columns:
                        max_length = 0
                        column_letter = column[0].column_letter
                        for cell in column:
                            try:
                                if len(str(cell.value)) > max_length:
                                    max_length = len(str(cell.value))
                            except Exception:
                                pass
                        adjusted_width = min(max_length + 2, 50)
                        worksheet.column_dimensions[column_letter].width = adjusted_width
                
                self.update_progress(f"✅ Created {excel_filename}", "", force_update=True)
                return True
                
            except Exception as e:
                self.update_progress(f"❌ Error creating {filename_base}", f"Error: {str(e)}")
                return False
        
        except Exception as e:
            self.update_progress(f"❌ Error in create_excel_file", f"Error: {str(e)}")
            return False

def show_completion_message(files_created, total_transactions):
    """Show completion message using GUI"""
    try:
        import tkinter as tk
        from tkinter import messagebox
        
        # Create a hidden root window
        root = tk.Tk()
        root.withdraw()
        
        # Show completion message
        if files_created > 0:
            message = f"✅ SUCCESS!\n\n" \
                     f"Created {files_created} Excel file(s)\n" \
                     f"Processed {total_transactions} transactions\n\n" \
                     f"Check the 'Excel' folder for your results!"
            title = "PDF to Excel Conversion - Complete"
        else:
            message = "⚠️ No Excel files were created.\n\n" \
                     "Please check that your PDFs contain transaction data\n" \
                     "and try again."
            title = "PDF to Excel Conversion - No Data Found"
        
        messagebox.showinfo(title, message)
        root.destroy()
        
    except Exception:
        # Fallback: console message
        try:
            if files_created > 0:
                print(f"✅ SUCCESS! Created {files_created} Excel file(s), Processed {total_transactions} transactions")
            else:
                print("⚠️ No Excel files were created.")
        except Exception:
            pass

def main():
    try:
        converter = UniversalPDFToExcelConverter()
        
        # Show progress window
        progress_window = converter.show_progress_window()
        
        files_created = 0
        total_transactions = 0
        
        try:
            if progress_window:
                # Run conversion directly in main thread to avoid variable scope issues
                files_created, total_transactions = converter.process_all_pdfs()
            else:
                # Fallback: run without GUI
                files_created, total_transactions = converter.process_all_pdfs()
                
        except Exception as e:
            converter.update_progress("❌ Critical error", f"Error: {str(e)}")
        
        # Close progress window
        converter.close_progress_window()
        
        # Show completion message with validation info
        show_completion_message_with_validation(converter, files_created, total_transactions)
        
    except Exception as e:
        try:
            print(f"Critical error: {str(e)}")
            time.sleep(3)
        except Exception:
            pass

def show_completion_message_with_validation(converter, files_created, total_transactions):
    """Enhanced completion message that includes validation summary"""
    try:
        import tkinter as tk
        from tkinter import messagebox
        
        # Create a hidden root window
        root = tk.Tk()
        root.withdraw()
        
        # Build validation summary
        validation_summary = ""
        if hasattr(converter, 'validator') and converter.validator.validation_results:
            validation_summary = "\n\n📊 VALIDATION SUMMARY:\n"
            
            total_files = len(converter.validator.validation_results)
            high_confidence = sum(1 for r in converter.validator.validation_results.values() if r['confidence_score'] >= 95)
            medium_confidence = sum(1 for r in converter.validator.validation_results.values() if 85 <= r['confidence_score'] < 95)
            low_confidence = sum(1 for r in converter.validator.validation_results.values() if r['confidence_score'] < 85)
            
            validation_summary += f"🟢 Excellent (95%+): {high_confidence} files\n"
            validation_summary += f"🟡 Good (85-94%): {medium_confidence} files\n"
            validation_summary += f"🔴 Needs Review (<85%): {low_confidence} files\n"
            
            # Count total potential issues
            total_missed = sum(len(r['potential_missed']) for r in converter.validator.validation_results.values())
            amount_issues = sum(1 for r in converter.validator.validation_results.values() if r['amount_discrepancy'])
            
            if total_missed > 0 or amount_issues > 0:
                validation_summary += f"\n⚠️  Issues Found:\n"
                if total_missed > 0:
                    validation_summary += f"   • {total_missed} potentially missed transactions\n"
                if amount_issues > 0:
                    validation_summary += f"   • {amount_issues} files with amount discrepancies\n"
                validation_summary += "\nCheck validation report for details!"
            else:
                validation_summary += "\n✅ No issues detected!"
        
        # Show completion message
        if files_created > 0:
            message = f"✅ SUCCESS!\n\n" \
                     f"Created {files_created} Excel file(s)\n" \
                     f"Processed {total_transactions} transactions\n\n" \
                     f"Check the 'Excel' folder for your results!" + validation_summary
            title = "PDF to Excel Conversion - Complete"
        else:
            message = "⚠️ No Excel files were created.\n\n" \
                     "Please check that your PDFs contain transaction data\n" \
                     "and try again." + validation_summary
            title = "PDF to Excel Conversion - No Data Found"
        
        messagebox.showinfo(title, message)
        root.destroy()
        
    except Exception:
        # Fallback: console message
        try:
            if files_created > 0:
                print(f"✅ SUCCESS! Created {files_created} Excel file(s), Processed {total_transactions} transactions")
                if hasattr(converter, 'validator') and converter.validator.validation_results:
                    print("📋 Validation report created - check Excel folder for details!")
            else:
                print("⚠️ No Excel files were created.")
        except Exception:
            pass

if __name__ == "__main__":
    main()