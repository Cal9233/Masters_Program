"""
DOB (Date of Birth) Module

This module provides functionality for collecting, validating, and formatting
date of birth information. It ensures that user inputs for day, month, and
year are valid before processing them.

Author: Calvin Malagon
Version: 1.0.0.0
Date: 5/12/25

Constituents:
    - DOB class: Handles date of birth data and validation
    - main function: Entry point for the program execution

Purpose:
    To collect and validate user birth date information and display it in a 
    formatted manner.

Dependencies:
    - Python's built-in input/output functions
    - Standard Python exception handling
"""

class DOB:
    """
    A class for handling Date of Birth information.
    
    Purpose:
        Manages the collection, validation, and formatting of date of birth data.
    
    Methods:
        - __init__: Constructor for initializing DOB object
        - get_bday: Formats and returns the birthdate as a string
        - get_valid_input: Static method for validating user input
        - validate_value: Static method for basic numeric validation
        - validate_day: Static method for day validation
        - validate_month: Static method for month validation
        - validate_year: Static method for year validation
    
    Attributes:
        day (int): The day of birth (1-31)
        month (int): The month of birth (1-12)
        year (int): The year of birth (typically 1900-2025)
    """
    
    def __init__(self, day=None, month=None, year=None):
        """
        Initialize a DOB object with optional day, month, and year.
        
        Function:
            Constructor that initializes the DOB object
        
        Input Parameters:
            day (int, optional): The day of birth. Defaults to None.
            month (int, optional): The month of birth. Defaults to None.
            year (int, optional): The year of birth. Defaults to None.
        
        Output Parameters:
            None
        """
        # Meaning: Components of birth date
        self.day = day      # Range: 1-31, represents day of month
        self.month = month  # Range: 1-12, represents month of year
        self.year = year    # Range: 1900-2025, represents year

    def get_bday(self):
        """
        Format the birthdate as a string.
        
        Function:
            Accessor method that returns formatted birthdate
            
        Input Parameters:
            None
            
        Output Parameters:
            str: A formatted string representation of the birthdate in MM/DD/YYYY format.
        """
        return f"Birthdate: {self.month}/{self.day}/{self.year}"
    
    @staticmethod
    def get_valid_input(prompt, validation_func, error_message):
        """
        Get and validate user input based on a custom validation function.
        
        Function:
            Static utility method for input validation
            
        Input Parameters:
            prompt (str): The message to display when asking for input.
            validation_func (callable): Function that validates input.
            error_message (str): Message to display on validation failure.
        
        Output Parameters:
            int: The validated input converted to an integer.
        """
        while True:
            try:
                value = input(prompt)
                if validation_func(value):
                    return int(value)
                else:
                    print(error_message)
            except ValueError:
                print("Invalid input.")

    @staticmethod
    def validate_value(val):
        """
        Validate that the input can be converted to an integer.
        
        Function:
            Static utility method for basic numeric validation
            
        Input Parameters:
            val (str): The input string to validate.
        
        Output Parameters:
            bool: True if the input can be converted to an integer, False otherwise.
        """
        try:
            int(val)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validate_day(val):
        """
        Validate that the input is a valid day (1-31).
        
        Function:
            Static utility method for day validation
            
        Input Parameters:
            val (str): The input string to validate.
        
        Output Parameters:
            bool: True if the input is a valid day, False otherwise.
        """
        # Meaning: Day range boundaries
        MIN_DAY = 1   # Minimum valid day
        MAX_DAY = 31  # Maximum valid day
        
        try:
            day = int(val)
            return MIN_DAY <= day <= MAX_DAY
        except ValueError:
            return False
    
    @staticmethod
    def validate_month(val):
        """
        Validate that the input is a valid month (1-12).
        
        Function:
            Static utility method for month validation
            
        Input Parameters:
            val (str): The input string to validate.
        
        Output Parameters:
            bool: True if the input is a valid month, False otherwise.
        """
        # Meaning: Month range boundaries
        MIN_MONTH = 1   # Minimum valid month
        MAX_MONTH = 12  # Maximum valid month
        
        try:
            month = int(val)
            return MIN_MONTH <= month <= MAX_MONTH
        except ValueError:
            return False
    
    @staticmethod
    def validate_year(val):
        """
        Validate that the input is a valid year (1900-2025).
        
        Function:
            Static utility method for year validation
            
        Input Parameters:
            val (str): The input string to validate.
        
        Output Parameters:
            bool: True if the input is a valid year, False otherwise.
        """
        # Meaning: Year range boundaries
        MIN_YEAR = 1900  # Minimum valid year
        MAX_YEAR = 2025  # Maximum valid year
        
        try:
            year = int(val)
            return MIN_YEAR <= year <= MAX_YEAR
        except ValueError:
            return False
    
def main():
    """
    Main function to run the DOB program.
    
    Function:
        Entry point for the application
        
    Input Parameters:
        None (reads from standard input)
        
    Output Parameters:
        None (writes to standard output)
    """
    print("Hello, this is a simple program made to accept user's input and outputs their birthday.")
    dob = DOB()
    
    dob.validate_day.__doc__
    # Use get_valid_input for day, month, and year
    month = dob.get_valid_input("Please enter your birth month (1-12): ", dob.validate_month, "Please enter a valid month (1-12).")
    day = dob.get_valid_input("Please enter your birth day (1-31): ", dob.validate_day, "Please enter a valid day (1-31).")
    year = dob.get_valid_input("Please enter your birth year (1900-2025): ", dob.validate_year, "Please enter a valid year (1900-2025).")
    
    # Update the DOB object with the validated inputs
    dob.month = month
    dob.day = day
    dob.year = year
    
    # Display the birthday
    print(dob.get_bday())

if __name__ == "__main__":
    main()