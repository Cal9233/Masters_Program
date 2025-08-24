from BLL import MRCBusinessLogic
from datetime import date, time

def print_header(title):
    """Print a formatted header for sections"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def print_subheader(title):
    """Print a formatted subheader"""
    print(f"\n--- {title} ---")

def format_table(data, headers):
    """Format data as a simple table"""
    if not data:
        return "No data to display"
    
    # Calculate column widths
    widths = [len(header) for header in headers]
    for row in data:
        for i, cell in enumerate(row):
            if i < len(widths):
                widths[i] = max(widths[i], len(str(cell)))
    
    # Create format string
    format_str = " | ".join(f"{{:<{width}}}" for width in widths)
    
    # Print header
    result = []
    result.append(format_str.format(*headers))
    result.append("-" * (sum(widths) + 3 * (len(headers) - 1)))
    
    # Print data
    for row in data:
        result.append(format_str.format(*[str(cell) for cell in row]))
    
    return "\n".join(result)

def display_revenue_data(revenue_data):
    """Display total revenue by vessel in a user-friendly format"""
    print_subheader("Total Revenue by Vessel")
    
    if isinstance(revenue_data, str):
        print(revenue_data)
        return
    
    if not revenue_data:
        print("No revenue data available")
        return
    
    # Format for table display
    table_data = [(item['vessel_name'], item['revenue']) for item in revenue_data]
    headers = ['Vessel Name', 'Total Revenue']
    
    print(format_table(table_data, headers))

def display_vessel_id_result(result):
    """Display vessel ID lookup result"""
    if "error" in result:
        print(f"Error: {result['error']}")
        return
    
    vessel_name = result['vessel_name']
    if result['found']:
        print(f"✓ {result['message']}")
    else:
        print(f"✗ {result['message']}")

def display_trips_data(trips_data):
    """Display all trips in a user-friendly format"""
    print_subheader("All Trips")
    
    if isinstance(trips_data, str):
        print(trips_data)
        return
    
    if not trips_data:
        print("No trips available")
        return
    
    # Format for table display
    table_data = []
    for trip in trips_data:
        table_data.append([
            trip['date_time'],
            trip['vessel_name'],
            trip['passenger_name'],
            trip['passenger_address'],
            trip['passenger_phone'],
            trip['total_cost']
        ])
    
    headers = ['Date & Time', 'Vessel', 'Passenger', 'Address', 'Phone', 'Cost']
    print(format_table(table_data, headers))

def get_database_credentials():
    """Get database connection parameters from user"""
    print_header("Marine Rental Company - Database Setup")
    print("Please provide your database connection details:")
    
    host = input("Database Host (default: localhost): ").strip() or "localhost"
    user = input("Database Username: ").strip()
    password = input("Database Password: ").strip()
    database = input("Database Name (default: mrc): ").strip() or "mrc"
    
    return host, user, password, database

def main():
    """Main application entry point"""
    print_header("Welcome to Marine Rental Company Management System")
    print("This application demonstrates database operations for the MRC system.")
    print("The system will showcase various database calls and display results in a user-friendly format.")
    
    # Initialize business logic
    mrc_bll = MRCBusinessLogic()
    
    try:
        # Get database credentials and connect
        print_subheader("Database Connection")
        host, user, password, database = get_database_credentials()
        
        print(f"\nConnecting to database '{database}' as user '{user}'...")
        if not mrc_bll.initialize_database_connection(user, password, database, host):
            print("Failed to connect to database. Please check your credentials and try again.")
            return
        
        # 6b. Call the 'Total Revenue by Vessel' view
        print_header("Total Revenue by Vessel")
        print("Retrieving total revenue data for each vessel...")
        revenue_data = mrc_bll.get_total_revenue_by_vessel()
        display_revenue_data(revenue_data)
        
        # 6c. Call getVesselID function twice - once with match, once without
        print_header("Vessel ID Lookups")
        print("Testing vessel ID lookup with existing and non-existing vessels...")
        
        print_subheader("Looking up existing vessel: 'Sea Breeze'")
        result1 = mrc_bll.get_vessel_id_with_validation("Sea Breeze")
        display_vessel_id_result(result1)
        
        print_subheader("Looking up non-existing vessel: 'Ghost Ship'")
        result2 = mrc_bll.get_vessel_id_with_validation("Ghost Ship")
        display_vessel_id_result(result2)
        
        # 6d. Call addTrip procedure twice
        print_header("Adding New Trips")
        
        print_subheader("Adding trip for existing vessel and passenger")
        print("Adding trip: Ocean Voyager with Emily Clark on 2025-08-15 at 14:00...")
        trip_result1 = mrc_bll.add_new_trip_existing_entities(
            vessel_name="Ocean Voyager",
            passenger_first_name="Emily",
            passenger_last_name="Clark",
            trip_date=date(2025, 8, 15),
            departure_time=time(14, 0),
            length_in_hours=2.5,
            total_passengers=4
        )
        print(f"Result: {trip_result1}")
        
        print_subheader("Adding trip with new vessel and passenger")
        print("Adding new vessel 'Deep Explorer' and passenger 'Alice Waters' with a trip...")
        trip_result2 = mrc_bll.add_new_trip_with_new_entities(
            vessel_name="Deep Explorer",
            vessel_cost_per_hour=175.00,
            passenger_first_name="Alice",
            passenger_last_name="Waters",
            passenger_phone="508-555-9876",
            trip_date=date(2025, 8, 16),
            departure_time=time(10, 30),
            length_in_hours=4.0,
            total_passengers=6
        )
        print(f"Result: {trip_result2}")
        
        # 6e. Call the 'All Trips' view
        print_header("Step 4: All Trips Display")
        print("Retrieving and displaying all trips...")
        trips_data = mrc_bll.get_all_trips_formatted()
        display_trips_data(trips_data)
        
        print_header("Demonstration Complete")
        print("Thank you for using the Marine Rental Company Management System!")
        print("All database operations have been completed successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Clean up database connection
        mrc_bll.close_connection()
        print("\nDatabase connection closed.")

if __name__ == "__main__":
    main()