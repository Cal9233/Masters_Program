#!/usr/bin/env python3
"""
Random Numbers Folder Creator
Author: Calvin Malagon
Date: 09/25/2025
OS: Windows
"""

import os
import random
import subprocess
import sys
import shutil

def check_folder_exists(folder_path):
    """Check if folder exists using system call."""
    if os.name == 'nt':  # Windows
        result = subprocess.run(['dir', folder_path], 
                              shell=True, 
                              capture_output=True, 
                              text=True)
        return result.returncode == 0

def remove_folder(folder_path):
    """Remove folder using system call."""
    try:
        if os.name == 'nt':  # Windows
            subprocess.run(['rmdir', '/s', '/q', folder_path], 
                         shell=True, 
                         check=True)
        print(f"Existing folder '{folder_path}' removed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error removing folder: {e}")
        sys.exit(1)

def create_folder(folder_path):
    """Create folder using system call."""
    try:
        if os.name == 'nt':  # Windows
            subprocess.run(['mkdir', folder_path], 
                         shell=True, 
                         check=True)
        print(f"Folder '{folder_path}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating folder: {e}")
        sys.exit(1)

def generate_random_numbers():
    """Generate 100 random numbers between 0 and 1000."""
    return [random.randint(0, 1000) for _ in range(100)]

def save_numbers_to_file(folder_path, numbers):
    """Save the random numbers to a file in the specified folder."""
    file_path = os.path.join(folder_path, "numbers100.txt")
    try:
        with open(file_path, 'w') as file:
            for number in numbers:
                file.write(f"{number}\n")
        print(f"100 random numbers saved to '{file_path}'")
    except IOError as e:
        print(f"Error saving file: {e}")
        sys.exit(1)

def main():
    """Main function to execute the program."""
    print("Random Numbers Folder Creator")
    print("=" * 30)
    
    # Get folder name from user
    folder_name = input("Enter the name of the folder to create: ").strip()
    
    if not folder_name:
        print("Error: Folder name cannot be empty.")
        sys.exit(1)
    
    # Get current working directory and create full path
    current_dir = os.getcwd()
    folder_path = os.path.join(current_dir, folder_name)
    
    print(f"Working in directory: {current_dir}")
    
    # Check if folder exists using system call
    if check_folder_exists(folder_path):
        print(f"Folder '{folder_name}' already exists.")
        remove_folder(folder_path)
    
    # Create the folder using system call
    create_folder(folder_path)
    
    # Generate 100 random numbers
    print("Generating 100 random numbers between 0 and 1000...")
    random_numbers = generate_random_numbers()
    
    # Save numbers to file
    save_numbers_to_file(folder_path, random_numbers)
    
    print("\nProgram completed successfully!")
    print(f"Summary:")
    print(f"- Folder created: {folder_path}")
    print(f"- File created: {os.path.join(folder_path, 'numbers100.txt')}")
    print(f"- Numbers generated: 100 random numbers (0-1000)")

if __name__ == "__main__":
    main()