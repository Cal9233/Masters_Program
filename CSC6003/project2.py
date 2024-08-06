#a loop to return error message if user continues to input incorrect value (inputs anything that is not a number)
def get_valid_input(prompt, validation_func, error_message):
    while True:
        try:
            value = input(prompt)
            if validation_func(value):
                return float(value)
            else:
                print(error_message)
        except ValueError:
            print("Invalid input.")

#validates if you're input is a number
def validate_value(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

#main program
def main():
    print("Hello!")


#continously reruns the program to try with different number unless user prompts not to do so
while True:
    main()
    choice = input('Would you like to try with different numbers? (y/n): ').strip().lower()
    while choice != 'y' and choice != 'n':
        choice = input('Please enter a valid response, would you like to try again with different numbers? (y/n): ').strip().lower()
    if choice != 'y':
        print('Goodbye!')
        break