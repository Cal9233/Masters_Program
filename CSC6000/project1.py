def valid_name(name):
    return not any(char.isdigit() for char in name)

def valid_age(age):
    return age.isdigit()

def valid_year(year):
    try:
        year_int = int(year)
        return 1000 <= year_int <= 9999
    except ValueError:
        return False

def calculate_age(age, year):
    birth_year = int(year) - int(age)
    return birth_year

print("Hello, please enter your name")
name = input("Enter a name: ")

if not valid_name(name):
    name = input("Please enter a valid name: ")

while True:
    print("Hello " + name + ", please enter your age")
    age = input("Enter age: ")

    if valid_age(age):
        break
    else:
        print("Please enter a valid age")

while True:
    print("And what year are we currently in?")
    year = input("Enter year: ")

    if valid_year(year):
        break
    else:
        print("Please enter a valid year")

birth_year1 = calculate_age(age, year)
birth_year2 = calculate_age(age, str(int(year) + 1))

print("Dear " + name + ", you were born in either " + str(birth_year1) + " or " + str(birth_year2))