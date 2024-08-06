def check_input(input_str):
    try:
        if isinstance(input_str, str):
            if len(input_str) == 0: return False
            for char in input_str:
                if not (char.isdigit() or 'A' <= char.upper() <= 'F'):
                    return False
            return True
        return True
    except ValueError:
        return False

def valid_base(b):
    try:
        if len(b) == 0: return False
        base = int(b)
        return 2 <= base <= 16
    except ValueError:
        return False

def convert_to_decimal(number, base):
    decimal = 0
    power = len(number) - 1
    for digit in number:
        if digit.isdigit():
            value = int(digit)
        else:
            value = ord(digit.upper()) - ord('A') + 10
        decimal += value * (base ** power)
        power -= 1
    return decimal

def main():
    string_num = input("Hello! Please enter a number in any base: ")

    if not isinstance(string_num, int):
        try:
            string_num = int(string_num)
        except ValueError:
            pass

    while not check_input(string_num):
        string_num = input("Please enter a valid number in any base: ")

    base = input("Now enter the base (between 2 and 16): ")

    while not valid_base(base):
        base = input("Please enter a valid base number between 2 and 16: ")

    decimal_representation = convert_to_decimal(str(string_num), int(base))
    binary_representation = bin(decimal_representation)[2:]

    print(f"The number {string_num} in base {base} is: {decimal_representation} in base 10 and {binary_representation} in base 2.")

while True:
    main()
    choice = input('Would you like to try with a different number? (y/n): ').strip().lower()
    while choice != 'y' and choice != 'n':
        choice = input('Please enter a valid response, would you like to try again with a different number? (y/n): ').strip().lower()
    if choice != 'y':
        print('Goodbye!')
        break