import math

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

# C (circumference) = 2πr
def circum(num):
    return 2 * math.pi * num

# A (Area) = πr^2
def area(num):
    return math.pi * num ** 2

# V (Volume) = 4/3 πr^3
def volume(num):
    return 4/3 * math.pi * num ** 3

#main program
def main():
    print("Hello!")
    #user radius value
    r = get_valid_input("Please enter the radius (number) of a circle/sphere: ", validate_value, "Please enter a valid number")
    #circumference result
    cirumResult = circum(r)
    #area result
    areaResult = area(r)
    #volume result
    volumeResult = volume(r)
    #print all results
    print(f"The circumference of a circle with a radius of {r} is {cirumResult}")
    print(f"The area of a circle with a radius of {r} is {areaResult}")
    print(f"The volume of a sphere with a radius of {r} is {volumeResult}")

#continously reruns the program to try with different number unless user prompts not to do so
while True:
    main()
    choice = input('Would you like to try with different numbers? (y/n): ').strip().lower()
    while choice != 'y' and choice != 'n':
        choice = input('Please enter a valid response, would you like to try again with different numbers? (y/n): ').strip().lower()
    if choice != 'y':
        print('Goodbye!')
        break