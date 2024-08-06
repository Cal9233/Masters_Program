def get_valid_input(prompt, validation_func, error_message):
    while True:
        try:
            value = input(prompt)
            if validation_func(value):
                return int(value)
            else:
                print(error_message)
        except ValueError:
            print("Invalid input. Please enter an integer.")

def validate_value(val):
    return val.isdigit()

def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def lottery_probabilities(n, k):
    total_combinations = combination(n, k)
    prob_win_big = 1 / total_combinations
    prob_win_little = (combination(k, k-1) * combination(n-k, 1)) / total_combinations
    
    return prob_win_big, prob_win_little

def main():
    print("Hello!")
    n = get_valid_input("Enter the total number of possible numbers (n): ", validate_value, "Please enter a valid number of possible numbers")
    k = get_valid_input("Enter the number of numbers to be guessed (k): ", validate_value, "Please enter a valid number of numbers to be guessed")
    
    if k > n:
        print("The number of guesses k cannot be greater than the total number of possible numbers n.")
        return
    
    prob_big, prob_little = lottery_probabilities(n, k)
    
    print(f"The probability of winning big (hitting all {k} drawn numbers) is: {prob_big:.10f}")
    print(f"The probability of winning little (hitting {k-1} drawn numbers) is: {prob_little:.10f}")

while True:
    main()
    choice = input('Would you like to try with different numbers? (y/n): ').strip().lower()
    while choice != 'y' and choice != 'n':
        choice = input('Please enter a valid response, would you like to try again with different numbers? (y/n): ').strip().lower()
    if choice != 'y':
        print('Goodbye!')
        break
