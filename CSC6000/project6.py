def get_valid_input(prompt, validation_func, error_message):
    while True:
        try:
            value = input(prompt)
            if validation_func(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print("Invalid input.")

def validate_value(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def generate_matrices(r, c, matrix_number):
    matrix = []
    for i in range(r):
        row = []
        for j in range(c):
            value = get_valid_input(f"For Matrix {matrix_number}, enter value for row {i+1}, column {j+1}: ", validate_value, "Invalid input. Please enter a valid number.")
            row.append(float(value))
        matrix.append(row)
    return matrix


def multiply_matrices(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            sum = 0
            for k in range(len(mat2)):
                sum += mat1[i][k] * mat2[k][j]
            row.append(sum)
        result.append(row)
    return result

def is_identity_matrix(matrix):
    n = len(matrix)
    tolerance = 1e-10  # This is to prevents small floating numbers from being identified as exact values 

    for i in range(n):
        for j in range(n):
            if i == j:
                if not (1 - tolerance <= matrix[i][j] <= 1 + tolerance):
                    return False
            else:
                if not (-tolerance <= matrix[i][j] <= tolerance):
                    return False
    return True

def check_inverse_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return False

    result1 = multiply_matrices(matrix1, matrix2)
    if not is_identity_matrix(result1):
        return False

    result2 = multiply_matrices(matrix2, matrix1)
    if not is_identity_matrix(result2):
        return False

    return True


def main():
    print("Hello!")
    matrix1_r = get_valid_input("Please input a number of rows for Matrix1: ", validate_value, "Invalid input. Please enter a valid number.")
    matrix1_c = get_valid_input("Please input a number of columns for Matrix1: ", validate_value, "Invalid input. Please enter a valid number.")
    matrix2_r = get_valid_input("Please input a number of rows for Matrix2: ", validate_value, "Invalid input. Please enter a valid number.")
    matrix2_c = get_valid_input("Please input a number of columns for Matrix2: ", validate_value, "Invalid input. Please enter a valid number.")

    matrix1_r = int(matrix1_r)
    matrix1_c = int(matrix1_c)
    matrix2_r = int(matrix2_r)
    matrix2_c = int(matrix2_c)

    matrix1 = generate_matrices(matrix1_r, matrix1_c, "1")
    matrix2 = generate_matrices(matrix2_r, matrix2_c, "2")

    if check_inverse_matrices(matrix1, matrix2):
        print("The matrices are inverses of each other.")
    else:
        print("The matrices are not inverses of each other.")

while True:
    main()
    choice = input('Would you like to try with different numbers? (y/n): ').strip().lower()
    while choice != 'y' and choice != 'n':
        choice = input('Please enter a valid response, would you like to try again with different numbers? (y/n): ').strip().lower()
    if choice != 'y':
        print('Goodbye!')
        break