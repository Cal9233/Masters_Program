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

def validate_value(val):
    return 4 <= val <= 8

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combine(n, r):
    ncr = factorial(n) // (factorial(r) * factorial(n - r))
    return ncr

def pascal_triangle(i):
    z = len(str(combine(i, (i // 2))))
    nosp = z * i

    for k in range(0, i + 1):
        sttr = ''
        for l in range(0, k + 1):
            sttr += (" " * (2 * z - len(str(combine(k, l))))) + str(combine(k, l))
        print(" " * nosp + sttr)
        nosp -= z

def main():
    print("Hello!")
    value = get_valid_input("Please input a number of lines (only from 4 to 8) for the Pascal's Triangle: ", validate_value, "Invalid input. Please enter a value between 4 and 8.")
    pascal_triangle(value)
while True:
    main()
    choice = input('Would you like to try with different numbers? (y/n): ').strip().lower()
    while choice != 'y' and choice != 'n':
        choice = input('Please enter a valid response, would you like to try again with different numbers? (y/n): ').strip().lower()
    if choice != 'y':
        print('Goodbye!')
        break