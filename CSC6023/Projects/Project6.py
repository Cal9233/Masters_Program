import numpy as np

def get_valid_input(prompt, input_type=float, arr_size=None):
    """Helper function to get and validate user input"""
    while True:
      try:
          print(prompt)
          if arr_size is None:
            return input_type(input().strip())
          else:
            values = [input_type(x) for x in input().strip().split()]
            if len(values) != arr_size:
              print(f"Please enter exactly {arr_size} values. (space-separated)")
              continue
            return values
      except ValueError:
        print("Invalid input. Please try again.")

def print_table(vars_count, obj_coeffs, A, b):
    """Print the problem setup in a tabular format"""
    print("\nProblem Setup:")
    print("-" * 50)
    header = "Variables |"
    for i in range(vars_count):
        header += f" Item {i+1} |"
    header += " Profit"
    print(header)
    print("-" * 50)
    
    for i in range(vars_count):
        row = f"Constraint {i+1}|"
        for j in range(vars_count):
            row += f" {A[i][j]:3} |"
        row += f" {obj_coeffs[i]}"
        print(row)
    
    print("-" * 50)
    limit = "Availability  |"
    for coeff in b:
        limit += f" {coeff:3} |"
    print(limit)
    print("-" * 50)

def calculate_solo_options(vars_count, obj_coeffs, A, b):
    """Calculate profit for each variable alone"""
    solo_results = []
    for var in range(vars_count):
        # Initialize solution vector with zeros
        solution = [0] * vars_count
        # Find limiting constraint for this variable
        min_ratio = float('inf')
        for i in range(vars_count):
            if A[i][var] > 0:
                ratio = b[i] / A[i][var]
                min_ratio = min(min_ratio, ratio)
        
        solution[var] = min_ratio
        profit = min_ratio * obj_coeffs[var]
        solo_results.append((solution, profit))
    return solo_results

def solve_linear_program(vars_count, obj_coeffs, A, b):
    """Main function to solve the linear programming problem"""
    print("\nCalculating solutions...\n")
    
    # Calculate solo options
    solo_results = calculate_solo_options(vars_count, obj_coeffs, A, b)
    
    # Calculate balanced solution using numpy
    try:
        A_np = np.array(A)
        b_np = np.array(b)
        balanced_solution = np.linalg.inv(A_np).dot(b_np)
        # Calculate profit for balanced solution
        balanced_profit = sum(s * c for s, c in zip(balanced_solution, obj_coeffs))
        
        # Find best solution
        all_profits = [profit for _, profit in solo_results]
        all_profits.append(balanced_profit)
        
        # Print results
        print("Solo Options:")
        for i, (solution, profit) in enumerate(solo_results):
            print(f"Option {i+1} (only item {i+1}): Units produced = {max(solution)}, Profit = {profit:.2f}")
        
        print(f"\nBalanced Solution:")
        print(f"Units produced = {[f'{x:.2f}' for x in balanced_solution]}")
        print(f"Profit = {balanced_profit:.2f}")
        
        best_profit = max(all_profits)
        if best_profit == balanced_profit:
            print(f"\nBest Option: Balanced solution with profit {balanced_profit:.2f}")
        else:
            best_idx = all_profits.index(best_profit)
            print(f"\nBest Option: Produce only item {best_idx + 1} with profit {best_profit:.2f}")
            
    except np.linalg.LinAlgError:
        print("Error: Could not solve the system. The matrix is singular.")
        return None


def main ():
    print("Linear Programming Solver")
    print("------------------------")

    # Get number of variables
    var_count = get_valid_input("Enter number of variables/constraints:", int)

    # Get objective function coefficients
    obj_coeffs = get_valid_input(
        f"Enter the {var_count} coefficients for the objective function (space-separated):", 
        float, 
        var_count
    )

    # Get constraint matrix
    # Rows = function
    # Example of input
    # Since f(x) = 2a + 4b + 5c = 300 -> Matrix Row: [2, 4, 5]
    # User input would be: 2 4 5
    print(f"\nEnter the {var_count}x{var_count} constraint matrix (one row at a time, space-separated):")
    A = []
    for i in range(var_count):
      row = get_valid_input(f"Row {i + 1}:", float, var_count)
      A.append(row)

    # Get constraint limits
    b = get_valid_input(
        f"Enter the {var_count} constraint limits (space-separated):", 
        float, 
        var_count
    )

    # Print the problem setup
    print_table(var_count, obj_coeffs, A, b)
    
    # Solve the problem
    solve_linear_program(var_count, obj_coeffs, A, b)

    print("------------------------")
if __name__ == "__main__":
  main()

# Chemical case
# Linear Programming Solver
# ------------------------
# Enter number of variables/constraints:
# 3
# Enter the 3 coefficients for the objective function (space-separated):
# 3000 2000 2000

# Enter the 3x3 constraint matrix (one row at a time, space-separated):
# Row 1:
# 2 4 5
# Row 2:
# 1 2 4
# Row 3:
# 8 0 3
# Enter the 3 constraint limits (space-separated):
# 300 200 300

# Problem Setup:
# --------------------------------------------------
# Variables | Item 1 | Item 2 | Item 3 | Profit
# --------------------------------------------------
# Constraint 1| 2.0 | 4.0 | 5.0 | 3000.0
# Constraint 2| 1.0 | 2.0 | 4.0 | 2000.0
# Constraint 3| 8.0 | 0.0 | 3.0 | 2000.0
# --------------------------------------------------
# Availability  | 300.0 | 200.0 | 300.0 |
# --------------------------------------------------

# Calculating solutions...

# Solo Options:
# Option 1 (only item 1): Units produced = 37.5, Profit = 112500.00
# Option 2 (only item 2): Units produced = 75.0, Profit = 150000.00
# Option 3 (only item 3): Units produced = 50.0, Profit = 100000.00

# Balanced Solution:
# Units produced = ['25.00', '20.83', '33.33']
# Profit = 183333.33

# Best Option: Balanced solution with profit 183333.33
# ------------------------

# Pants Jacket case

# Linear Programming Solver
# ------------------------
# Enter number of variables/constraints:
# 2
# Enter the 2 coefficients for the objective function (space-separated):
# 50 40

# Enter the 2x2 constraint matrix (one row at a time, space-separated):
# Row 1:
# 1 1.5
# Row 2:
# 2 1
# Enter the 2 constraint limits (space-separated):
# 750 1000

# Problem Setup:
# --------------------------------------------------
# Variables | Item 1 | Item 2 | Profit
# --------------------------------------------------
# Constraint 1| 1.0 | 1.5 | 50.0
# Constraint 2| 2.0 | 1.0 | 40.0
# --------------------------------------------------
# Availability  | 750.0 | 1000.0 |
# --------------------------------------------------

# Calculating solutions...

# Solo Options:
# Option 1 (only item 1): Units produced = 500.0, Profit = 25000.00
# Option 2 (only item 2): Units produced = 500.0, Profit = 20000.00

# Balanced Solution:
# Units produced = ['375.00', '250.00']
# Profit = 28750.00

# Best Option: Balanced solution with profit 28750.00