import csv
import os

def calculate_volume(height, width, depth):
    """Calculate volume of an item."""
    return height * width * depth

def knapsack_volume(items, capacity):
    """
    Greedy knapsack algorithm optimizing for value per volume.
    Returns distribution of items and remaining space.
    """
    # Calculate value per volume ratio for each item
    item_ratios = []
    for item in items:
        volume = calculate_volume(item['height'], item['width'], item['depth'])
        ratio = item['value'] / volume
        item_ratios.append({
            'name': item['name'],
            'value': item['value'],
            'volume': volume,
            'ratio': ratio
        })
    
    # Sort by value/volume ratio
    item_ratios.sort(key=lambda x: x['ratio'], reverse=True)
    
    # Initialize results
    distribution = {item['name']: 0 for item in items}
    total_value = 0
    remaining_space = capacity
    
    # Fill knapsack greedily
    found = True
    while found:
        found = False
        for item in item_ratios:
            if item['volume'] <= remaining_space:
                distribution[item['name']] += 1
                total_value += item['value']
                remaining_space -= item['volume']
                found = True
                break
    
    return distribution, total_value, remaining_space

def read_items(filename):
    """Read items from CSV file."""
    items = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            items.append({
                'name': row[0],
                'value': int(row[1]),
                'height': int(row[2]),
                'width': int(row[3]),
                'depth': int(row[4])
            })
    return items

def format_output(distribution, total_value, remaining_space):
    """Format the output string."""
    # Filter out items with quantity 0
    included_items = [(name, qty) for name, qty in distribution.items() if qty > 0]
    
    # Format items string
    if len(included_items) > 1:
        items_str = f"{included_items[0][1]} {included_items[0][0]} and {included_items[1][1]} {included_items[1][0]}"
    else:
        items_str = f"{included_items[0][1]} {included_items[0][0]}"
    
    return (f"The suggested items are: {items_str}, "
            f"with a total value of ${total_value}. "
            f"There were {remaining_space} cubic inches left unused.")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Read input file
    filename = "items.csv"  # Your input file name
    items = read_items(filename)
    
    # Get capacity from user
    capacity = int(input("Enter the package capacity (in cubic inches): "))
    
    # Solve knapsack problem
    distribution, total_value, remaining_space = knapsack_volume(items, capacity)
    
    # Print results
    print(format_output(distribution, total_value, remaining_space))

if __name__ == "__main__":
    main()