import random

#a loop to return error message if user continues to input incorrect value (inputs anything that is not a number)
def get_valid_input(prompt, validation_func, error_message):
    while True:
        value = input(prompt)
        if validation_func(value):
            return int(value)
        else:
            print(error_message)

#validates if input is a positive number
def validate_value(val):
    try:
        value = int(val)
        return 1 <= value <= 100
    except ValueError:
        return False
    
#Generate a random number between 1 and 100.
def generate_random_number(min, max):
    return random.randint(min, max)
    
#Checks if the user's guess matches the random number.
def check_guess(random_number, user_number):
    return random_number == user_number


#main program
def main():
    print("Hello! Welcome to the Guess the Number Game!")
    print("I have selected a random number between 1 and 100. Try to guess it!")
    #generate a random number between 1 and 100
    random_number = generate_random_number(1, 100)    
    #amount of guesses it took
    attempts = 0
    while True:
        #user inputs numbers, function validates if it is valid input
        user_number = get_valid_input("Guess the random number: ", validate_value, "Invalid input. Please enter a valid number that is between 1 and 100.")
        #increment attempts if user fails to guess random number
        attempts+= 1

        #returns True if the user's guess matches the random number, False otherwise
        if check_guess(random_number, user_number):
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break
        else:
            if user_number < random_number:
                print("Incorrect! Try a higher number.")
            else:
                print("Incorrect! Try a lower number.")

#continously reruns the program to try with different number unless user prompts not to do so
while True:
    main()
    choice = input('Would you like to try with different numbers? (y/n): ').strip().lower()
    while choice != 'y' and choice != 'n':
        choice = input('Please enter a valid response, would you like to try again with different numbers? (y/n): ').strip().lower()
    if choice != 'y':
        print('Goodbye!')
        break