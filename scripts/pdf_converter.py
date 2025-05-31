import os
import pdfplumber
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
import re

class PDFToExcelConverter:
    def __init__(self):
        self.convert_folder = "Convert"
        self.output_folder = None
        
    def setup_folders(self):
        """Create the Convert folder if it doesn't exist"""
        if not os.path.exists(self.convert_folder):
            os.makedirs(self.convert_folder)
            print(f"Created '{self.convert_folder}' folder. Place your PDF files here.")
            
    def get_output_directory(self):
        """Let user choose output directory"""
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        
        output_dir = filedialog.askdirectory(
            title="Select folder to save Excel files",
            initialdir=os.getcwd()
        )
        
        if not output_dir:
            print("No output directory selected. Using current directory.")
            return os.getcwd()
        
        return output_dir
    
    def extract_pdf_content(self, pdf_path):
        """Extract transaction data from Account Activity sections"""
        extracted_data = []
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    text = page.extract_text()
                    if text:
                        transactions = self.parse_account_activity(text, page_num)
                        extracted_data.extend(transactions)
        
        except Exception as e:
            print(f"Error processing {pdf_path}: {str(e)}")
            return None
            
        return extracted_data
    
    def parse_account_activity(self, text, page_num):
        """Parse transactions from Account Activity sections"""
        transactions = []
        lines = text.split('\n')
        in_activity_section = False
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Check if we're entering an Account Activity section
            if 'ACCOUNT ACTIVITY' in line.upper():
                in_activity_section = True
                continue
            
            # Check if we're leaving the activity section
            if in_activity_section and (
                line.startswith('INTEREST CHARGES') or
                line.startswith('FEES') or 
                line.startswith('2024 Totals') or
                line.startswith('YOUR ACCOUNT MESSAGES') or
                line.startswith('LUIS RODRIGUEZ') or
                line.startswith('JUAN LUIS RODRIGUEZ') or
                line.startswith('RODRIGUEZ GUTIERREZ') or
                line.startswith('PULAK UNG') or
                line.startswith('JOSE RODRIGUEZ') or
                line.startswith('ISABEL RODRIGUEZ') or
                'TRANSACTIONS THIS CYCLE' in line
            ):
                in_activity_section = False
                continue
            
            # Parse transaction lines within the activity section
            if in_activity_section and line and not line.startswith('Date of') and not line.startswith('Transaction'):
                transaction = self.parse_transaction_line(line, page_num)
                if transaction:
                    transactions.append(transaction)
        
        return transactions
    
    def parse_transaction_line(self, line, page_num):
        """Parse individual transaction line"""
        # Skip header lines and non-transaction lines
        if (line.startswith('Merchant Name') or 
            line.startswith('$ Amount') or
            line.startswith('&') or
            line.startswith('Your next Fixed') or
            line.startswith('Transactions designated') or
            len(line.strip()) < 10):
            return None
        
        # Pattern to match: Date + Merchant/Description + Amount
        # Looking for pattern like: MM/DD MERCHANT NAME $amount or -$amount
        date_pattern = r'^(\d{2}/\d{2})'
        amount_pattern = r'([-]?\$?[\d,]+\.\d{2})$'
        
        date_match = re.search(date_pattern, line)
        amount_match = re.search(amount_pattern, line)
        
        if date_match and amount_match:
            date = date_match.group(1)
            amount_str = amount_match.group(1)
            
            # Extract merchant/description (everything between date and amount)
            start_pos = date_match.end()
            end_pos = amount_match.start()
            merchant_desc = line[start_pos:end_pos].strip()
            
            # Clean up the merchant description
            merchant_desc = re.sub(r'\s+', ' ', merchant_desc)  # Remove extra spaces
            merchant_desc = merchant_desc.replace('&', '').strip()  # Remove & symbols
            
            # Clean up amount
            amount_str = amount_str.replace('$', '').replace(',', '')
            
            if merchant_desc and len(merchant_desc) > 2:  # Valid merchant name
                # Add year to date (assuming 2024 for now)
                full_date = f"{date}/24"
                
                return {
                    'Date': full_date,
                    'Merchant': merchant_desc,
                    'Amount': amount_str
                }
        
        return None
    
    def process_all_pdfs(self):
        """Process all PDFs in the Convert folder"""
        # Setup
        self.setup_folders()
        
        # Check for PDF files
        pdf_files = [f for f in os.listdir(self.convert_folder) if f.lower().endswith('.pdf')]
        
        if not pdf_files:
            print(f"No PDF files found in '{self.convert_folder}' folder.")
            print("Please add PDF files to the folder and run the script again.")
            return
        
        print(f"Found {len(pdf_files)} PDF file(s): {', '.join(pdf_files)}")
        
        # Get output directory
        self.output_folder = self.get_output_directory()
        print(f"Output directory: {self.output_folder}")
        
        # Process each PDF
        all_data = []
        
        for pdf_file in pdf_files:
            pdf_path = os.path.join(self.convert_folder, pdf_file)
            print(f"Processing: {pdf_file}")
            
            # Extract content
            pdf_data = self.extract_pdf_content(pdf_path)
            
            if pdf_data:
                all_data.extend(pdf_data)
                print(f"  ✓ Extracted {len(pdf_data)} transactions from {pdf_file}")
            else:
                print(f"  ✗ Failed to process {pdf_file}")
        
        if not all_data:
            print("No data extracted from any PDF files.")
            return
        
        # Create Excel file
        self.create_excel_file(all_data)
    
    def create_excel_file(self, data):
        """Create Excel file with extracted data"""
        # Create DataFrame with the three columns we want
        df = pd.DataFrame(data)
        
        # Generate filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        excel_filename = f"Credit_Card_Transactions_{timestamp}.xlsx"
        excel_path = os.path.join(self.output_folder, excel_filename)
        
        # Save to Excel
        try:
            with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Transactions', index=False)
                
                # Auto-adjust column widths
                worksheet = writer.sheets['Transactions']
                for column in worksheet.columns:
                    max_length = 0
                    column_letter = column[0].column_letter
                    for cell in column:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    adjusted_width = min(max_length + 2, 50)  # Cap at 50 characters
                    worksheet.column_dimensions[column_letter].width = adjusted_width
            
            print(f"\n✓ Successfully created Excel file: {excel_filename}")
            print(f"  Location: {excel_path}")
            print(f"  Total transactions: {len(df)}")
            
            # Show completion message
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo(
                "Conversion Complete", 
                f"Successfully extracted {len(df)} transactions\n"
                f"Excel file saved to:\n{excel_path}"
            )
            
        except Exception as e:
            print(f"Error creating Excel file: {str(e)}")

def main():
    print("=== Credit Card PDF to Excel Converter ===")
    print("Instructions:")
    print("1. Place all PDF files in the 'Convert' folder")
    print("2. Run this script")
    print("3. Choose output directory for Excel file")
    print("4. Wait for processing to complete")
    print("-" * 40)
    
    converter = PDFToExcelConverter()
    converter.process_all_pdfs()
    
    print("\nPress Enter to exit...")
    input()

if __name__ == "__main__":
    main()