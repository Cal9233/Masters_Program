import csv
import os

def calc_volume(h, w, d):
    """Calculate volume of an item."""
    return h * w * d

def knapsack(val, vol, cap):
    """Greedy knapsack algorithm implementation."""
    # array of values, array of weights
    rwv = []         # triplet ratio, weight, value, index
    for i in range(len(val)):
        rwv.append([val[i]/vol[i], vol[i], val[i], i])
    rwv.sort(reverse=True)    # sort from high to low rate
    ans = []                     # the list of added items
    tw = 0                                  # total weight
    found = True
    while (found):        # until no fitting item is found
        found = False
        for t in rwv:              # search an item to add
            if (t[1] + tw) <= cap:      # if the item fits
                ans.append(t[3])                  # add it
                tw += t[1]
                found = True
                break
    return ans           # returns the list of added items

def read_items(filename):
    """Read items from CSV file."""
    items = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            items.append({
                'name': row[0],
                'value': int(row[1]),
                'height': int(row[2]),
                'width': int(row[3]),
                'depth': int(row[4])
            })
    return items

def knapsack_helper(items):
    """Prepare arrays for knapsack function."""
    val_arr = []
    vol_arr = []
    for item in items:
        val_arr.append(item['value'])
        vol_arr.append(calc_volume(item['height'], item['width'], item['depth']))
    return val_arr, vol_arr

def distribute_helper(items, selected):
    """Create distribution dictionary from selected indices."""
    distribution = {item['name']: 0 for item in items}
    total_val = 0
    used_space = 0
    
    for index in selected:
        item = items[index]
        distribution[item['name']] += 1
        total_val += item['value']
        used_space += calc_volume(item['height'], item['width'], item['depth'])
    
    return distribution, total_val, used_space

def format_helper(distribution, total_val, remaining_space):
    """Format the output string."""
    # Filter out items with quantity 0
    included = [(name, qty) for name, qty in distribution.items() if qty > 0]
    
    # Format items string
    if len(included) > 1:
        items_str = f"{included[0][1]} {included[0][0]} and {included[1][1]} {included[1][0]}"
    else:
        items_str = f"{included[0][1]} {included[0][0]}" if included else "no items"
    
    return (f"The suggested items are: {items_str}, "
            f"with a total value of ${total_val}. "
            f"There were {remaining_space} cubic inches left unused.")

def main():
    # location of file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Read input file
    filename = "items.csv"
    items = read_items(filename)
    
    # Get capacity from user
    capacity = int(input("Enter the package capacity (in cubic inches): "))
    
    # Prepare input for knapsack
    val, vol = knapsack_helper(items)
    
    # Solve knapsack problem
    selected = knapsack(val, vol, capacity)
    
    # Create distribution from selected indices
    distribution, total_val, used_space = distribute_helper(items, selected)
    remaining_space = capacity - used_space
    
    # Print results
    print(format_helper(distribution, total_val, remaining_space))

if __name__ == "__main__":
    main()