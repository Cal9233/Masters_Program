from DAL import DBConnection, Vessel, Passenger, Trip
from datetime import date, time
from decimal import Decimal

class MRCBusinessLogic:
    def __init__(self):
        self.db_connection = None
    
    def initialize_database_connection(self, user, password, database, host='localhost'):
        """Initialize database connection with provided credentials"""
        self.db_connection = DBConnection(host=host, user=user, password=password, database=database)
        return self.db_connection.connect()
    
    def close_connection(self):
        """Close database connection"""
        if self.db_connection:
            self.db_connection.close()
    
    def get_total_revenue_by_vessel(self):
        """Get formatted total revenue by vessel data"""
        if not self.db_connection:
            return "Database connection not established"
        
        revenue_data = Trip.get_total_revenue_by_vessel(self.db_connection)
        
        if not revenue_data:
            return "No revenue data found"
        
        return revenue_data
    
    def get_vessel_id_with_validation(self, vessel_name):
        """Get vessel ID with business logic validation"""
        if not self.db_connection:
            return {"error": "Database connection not established"}
        
        if not vessel_name or vessel_name.strip() == "":
            return {"error": "Vessel name cannot be empty"}
        
        vessel_id = Vessel.get_vessel_id(vessel_name, self.db_connection)
        
        if vessel_id == -1:
            return {
                "vessel_name": vessel_name,
                "vessel_id": None,
                "found": False,
                "message": f"Vessel '{vessel_name}' not found in database"
            }
        else:
            return {
                "vessel_name": vessel_name,
                "vessel_id": vessel_id,
                "found": True,
                "message": f"Vessel '{vessel_name}' found with ID: {vessel_id}"
            }
    
    def add_new_trip_existing_entities(self, vessel_name, passenger_first_name, passenger_last_name,
                                     trip_date, departure_time, length_in_hours, total_passengers):
        """Add a trip for existing vessel and passenger with business validation"""
        if not self.db_connection:
            return "Database connection not established"
        
        # Validate inputs
        if not all([vessel_name, passenger_first_name, passenger_last_name, trip_date, departure_time]):
            return "All required fields must be provided"
        
        if length_in_hours <= 0:
            return "Trip length must be greater than 0"
        
        if total_passengers <= 0:
            return "Total passengers must be greater than 0"
        
        # Add the trip
        result = Trip.add_trip(
            vessel_name, passenger_first_name, passenger_last_name,
            trip_date, departure_time, length_in_hours, total_passengers,
            self.db_connection
        )
        
        # Interpret result
        if isinstance(result, int):
            if result == 0:
                return f"Error: Duplicate trip found for {vessel_name} on {trip_date} at {departure_time}"
            elif result == -1:
                return f"Error: Vessel '{vessel_name}' not found"
            elif result == -2:
                return f"Error: Passenger '{passenger_first_name} {passenger_last_name}' not found"
            elif result == -3:
                return f"Error: Both vessel '{vessel_name}' and passenger '{passenger_first_name} {passenger_last_name}' not found"
        
        return f"Trip successfully added for {vessel_name} with {passenger_first_name} {passenger_last_name}"
    
    def add_new_trip_with_new_entities(self, vessel_name, vessel_cost_per_hour,
                                     passenger_first_name, passenger_last_name, passenger_phone,
                                     trip_date, departure_time, length_in_hours, total_passengers):
        """Add a trip with new vessel and passenger"""
        if not self.db_connection:
            return "Database connection not established"
        
        # First, add the new vessel
        vessel_id = Vessel.add_vessel(vessel_name, vessel_cost_per_hour, self.db_connection)
        if vessel_id == -1:
            return f"Error adding vessel '{vessel_name}'"
        
        # Then, add the new passenger
        passenger_id = Passenger.add_passenger(passenger_first_name, passenger_last_name, passenger_phone, self.db_connection)
        if passenger_id == -1:
            return f"Error adding passenger '{passenger_first_name} {passenger_last_name}'"
        
        # Finally, add the trip
        result = Trip.add_trip(
            vessel_name, passenger_first_name, passenger_last_name,
            trip_date, departure_time, length_in_hours, total_passengers,
            self.db_connection
        )
        
        return f"Successfully added new vessel '{vessel_name}', passenger '{passenger_first_name} {passenger_last_name}', and trip"
    
    def get_all_trips_formatted(self):
        """Get all trips with user-friendly formatting"""
        if not self.db_connection:
            return "Database connection not established"
        
        trips = Trip.get_all_trips(self.db_connection)
        
        if not trips:
            return "No trips found"
        
        return trips
    
    def format_currency(self, amount):
        """Format currency for display"""
        if isinstance(amount, str) and amount.startswith('$'):
            return amount
        return f"${amount:,.2f}"
    
    def validate_date_format(self, date_str):
        """Validate and convert date string to date object"""
        try:
            return date.fromisoformat(date_str)
        except ValueError:
            return None
    
    def validate_time_format(self, time_str):
        """Validate and convert time string to time object"""
        try:
            return time.fromisoformat(time_str)
        except ValueError:
            return None