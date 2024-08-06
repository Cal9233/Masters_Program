def series_converges(r):
    try:
        return abs(r) < 1
    except ValueError:
        return False

def converging_sum(a, r):
    try:
        gp_sum = a / (1 - r)
        return gp_sum
    except ValueError:
        return None

def GP_infinite(a, r, n):
    try:
        if abs(r) >= 1:
            if r == 1:
                gp_sum = a * n
                return gp_sum
            else:
                gp_sum = a * (r ** n - 1) / (r - 1)
                return gp_sum
        else:
            gp_sum = a / (1 - r)
            return gp_sum
    except ValueError:
        return None
    
def convert_if_whole_number(value):
    if isinstance(value, float):
        if value.is_integer():
            return int(value)
    return value
    
def main():
    print("Hello")
    a = float(input("Enter the scale factor (a): "))
    r = float(input("Enter the common ratio (r): "))
    converges = series_converges(r)
    if converges:
        gp_sum = converging_sum(a, r)
        print(f"This GP converges with infinite elements to {convert_if_whole_number(gp_sum)}")
        print("The first terms are", end=" ")
        print(convert_if_whole_number(a), end=", ")
        print(convert_if_whole_number(a * r), end=", ")
        print(convert_if_whole_number(a * r **2))
    else: 
        print("This GP does not converge to a finite number with infinite elements")
        n = int(input("Please enter the number of elements (n): "))
        gp_sum = GP_infinite(a, r, n)
        if gp_sum is not None:
            print(f"This GP sum with {convert_if_whole_number(n)} elements is equal to {convert_if_whole_number(gp_sum)}")
            print("The first elements are", end=" ")
            print(convert_if_whole_number(a), end=", ")
            print(convert_if_whole_number(a * r), end=", ")
            print(convert_if_whole_number(a * r **2))
        else:
            print("This GP does not converge to a finite number with infinite elements")

while True:
    main()
    choice = input('Would you like to try with a different number? (y/n): ').strip().lower()
    while choice != 'y' and choice != 'n':
        choice = input('Please enter a valid response, would you like to try again with a different number? (y/n): ').strip().lower()
    if choice != 'y':
        print('Goodbye!')
        break