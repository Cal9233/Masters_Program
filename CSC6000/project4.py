#validates user input
def get_valid_input(prompt, validation_func, error_message):
    while True:
        try:
            value = int(input(prompt))
            if validation_func(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print("Invalid input. Please enter an integer.")

def validJ(j):
    return 3 <= j <= 8

def validM(m):
    return 1 <= m <= 5

def validK(k, n):
    return 1 <= k <= n

#factorial n!
def factorial(n):
    acc = 1
    for i in range(2, n + 1):
        acc *= i
    return acc

#Formula A = n! / (n - k)! * m1! * m2! . . mj!
def permutation(n, k, subsets):
    if len(subsets) == 0 or subsets is None:
        return 0
    if k > n:
        return 0
    denominator = 1
    for mi in subsets:
        denominator *= factorial(mi)
    return factorial(n) // (factorial(n - k) * denominator)

def main():
    print("Hello!")
    # Ask the user for the number of subsets (no smaller than 3, no greater than 8)
    j = get_valid_input("Please enter a number of subsets (no smaller than 3, no greater than 8): ", validJ, "Invalid input. Please enter a number between 3 and 8.")
    
    # Ask the user for the size of each subset
    subsets = []
    for i in range(j):
        mi = get_valid_input(f"Enter the size of subset {i + 1} (between 1 and 5): ", validM, "Invalid input. Please enter a number between 1 and 5.")
        subsets.append(mi)
    
    # Calculate the total number of elements in all subsets
    n = sum(subsets)
    # Ask the user for the size of the arrangement
    k = get_valid_input(f"Enter the number of elements to arrange (less than {n}): ", lambda x: validK(x, n), f"Invalid input. Please enter a number less than {n}.")
    
    # Compute and print the number of arrangements of k elements out of n
    total_permutations = permutation(n, k, subsets)
    print(f"Given your inputs, the number of arrangements is {total_permutations}")

while True:
    main()
    choice = input('Would you like to try with different numbers? (y/n): ').strip().lower()
    while choice != 'y' and choice != 'n':
        choice = input('Please enter a valid response, would you like to try again with different numbers? (y/n): ').strip().lower()
    if choice != 'y':
        print('Goodbye!')
        break