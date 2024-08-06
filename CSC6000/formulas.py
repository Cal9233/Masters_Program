#Week 2

#Natural number is any positive integer starting from 1
#Integer number is a whole number which can be negative, positive, or zero
#Real numbers are numbers that stay continuous, including all rational and irrational numbers
# def Natural_Real_Integer(n):
#     try:
#         num = float(n)

#         if num.is_integer():
#             num = int(num)
        
#         is_natural = num > 0 and isinstance(num, int)
#         is_integer = isinstance(num, int)
#         is_real = isinstance(num, (int, float))

#         if is_natural:
#             if is_integer and is_real:
#                 print("Natural, Integer, or Real")
#             elif is_integer:
#                 print("Natural or Integer")
#             elif is_real:
#                 print("Natural or Real")
#             else:
#                 print("Natural")
#         elif is_integer:
#             if is_real:
#                 print("Integer or Real")
#             else:
#                 print("Integer")
#         elif is_real:
#             print("Real")
#         else:
#             print("Unknown")
#     except ValueError:
#         print("Invalid input")

# user_input = input("Enter a number: ")
# Natural_Real_Integer(user_input)

#Prime is a number that can only be divided by 1 or itself
#Composite is a number that can be divided by varies factores as well as itself and 1
#Prime Numbers Example: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293
#Composite Numbers Example: 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100.
def Prime_or_Composite(n):
    n = int(input("Enter a number: "))
    pc = True
    for i in range(n // 2, 1, -1):
        if n % i == 0:
            pc = False
            break
    
    if pc == True:
        print("Prime")
    else:
        print("Composite")

user_input = input("Enter a number: ")
Prime_or_Composite(user_input)