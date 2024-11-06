import os

class Item:
    def __init__(self, name, value, height, width, depth):
        self.name = name
        self.value = float(value)
        self.height = float(height)
        self.width = float(width)
        self.depth = float(depth)
        self.volume = self.height * self.width * self.depth
        self.value_density = self.value / self.volume  # $ per cubic inch

def read_items(filename):
    """Read items from a file with format: name,value,height,width,depth"""
    items = []
    with open(filename, 'r') as file:
        for line in file:
            name, value, height, width, depth = line.strip().split(',')
            items.append(Item(name, value, height, width, depth))
    return items

def optimize_value(items, total_volume):
    """
    Optimize for maximum value within volume constraint using greedy approach
    Returns selected items and their quantities
    """
    # Sort items by value density (value per cubic inch)
    items_sorted = sorted(items, key=lambda x: x.value_density, reverse=True)
    
    selected = {}  # Dictionary to store item name and quantity
    remaining_volume = total_volume
    total_value = 0
    
    for item in items_sorted:
        # Calculate how many of this item can fit
        quantity = int(remaining_volume / item.volume)
        
        if quantity > 0:
            selected[item.name] = quantity
            volume_used = quantity * item.volume
            remaining_volume -= volume_used
            total_value += quantity * item.value
    
    return selected, total_value, remaining_volume

def format_results(selected, total_value, remaining_volume):
    """Format results into a readable string"""
    if not selected:
        return "No items could fit within the volume constraint."
    
    items_list = []
    for name, quantity in selected.items():
        items_list.append(f"{quantity} {name}")
    
    items_str = " and ".join(items_list)
    return (f"The suggested items are: {items_str} "
           f"with a total value of ${total_value:.2f}. "
           f"There were {remaining_volume:.2f} cubic inches left unused.")

def main():
    # Setup file path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    try:
        # Get volume constraint from user
        total_volume = float(input("Enter the total volume constraint (cubic inches): "))
        
        # Read items from file
        items = read_items('item_list.csv')
        
        # Optimize for value
        selected, total_value, remaining_volume = optimize_value(items, total_volume)
        
        # Print results
        result = format_results(selected, total_value, remaining_volume)
        print(result)
        
    except FileNotFoundError:
        print("Error: item_list.txt file not found in the current directory")
    except ValueError as e:
        print(f"Error: Invalid input - {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()