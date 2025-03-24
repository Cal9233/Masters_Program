#include <iostream>
using namespace std;

void printProduct(int **mat1, int **mat2, int r1, int c1, int r2, int c2)
{
    if (c1 != r2)
    {
        cout << "Impossible: Number of columns in first matrix is "
             << c1 << " and the number of rows in the second matrix is "
             << r2 << endl;
    }
    else
    {
        int result[r1][c2];
        cout << "Multiplication of given two matrices is:\n";

        // Calculate the results first
        for (int i = 0; i < r1; i++)
        {
            for (int j = 0; j < c2; j++)
            {
                result[i][j] = 0;
                for (int k = 0; k < c1; k++)
                {
                    result[i][j] += mat1[i][k] * mat2[k][j];
                }
            }
        }

        // Display in the format [ a b ] x [ c d ] = result
        for (int i = 0; i < r1; i++)
        {
            for (int j = 0; j < c2; j++)
            {
                // Print the first row of the multiplication
                cout << "[ ";
                for (int k = 0; k < c1; k++)
                {
                    cout << mat1[i][k];
                    if (k < c1 - 1)
                        cout << " ";
                }
                cout << " ] x [ ";

                // Print the column from the second matrix
                for (int k = 0; k < r2; k++)
                {
                    cout << mat2[k][j];
                    if (k < r2 - 1)
                        cout << " ";
                }
                cout << " ] = " << result[i][j] << endl;
            }
        }

        // Print just the result matrix in a cleaner format
        cout << "Result Matrix:" << endl;
        for (int i = 0; i < r1; i++)
        {
            for (int j = 0; j < c2; j++)
            {
                cout << result[i][j] << "\t";
            }
            cout << endl;
        }
    }
}

void exercise1(int r1, int c1, int r2, int c2)
{
    // Matrix 1
    int **mat1 = new int *[r1];
    for (int i = 0; i < r1; i++)
    {
        mat1[i] = new int[c1];
    }
    mat1[0][0] = 2;
    mat1[0][1] = 5;

    mat1[1][0] = 3;
    mat1[1][1] = 8;

    // Matrix 2
    int **mat2 = new int *[r2];
    for (int i = 0; i < r2; i++)
    {
        mat2[i] = new int[c2];
    }
    mat2[0][0] = 6;
    mat2[0][1] = 9;
    mat2[0][2] = 11;
    mat2[0][3] = 13;

    mat2[1][0] = 12;
    mat2[1][1] = 18;
    mat2[1][2] = 22;
    mat2[1][3] = 26;

    printProduct(mat1, mat2, r1, c1, r2, c2);
}

void exercise2(int r1, int c1, int r2, int c2)
{
    // Matrix 1
    int **mat1 = new int *[r1];
    for (int i = 0; i < r1; i++)
    {
        mat1[i] = new int[c1];
    }
    mat1[0][0] = 1;
    mat1[0][1] = 2;
    mat1[0][2] = 4;

    mat1[1][0] = 8;
    mat1[1][1] = 16;
    mat1[1][2] = 32;

    mat1[2][0] = 64;
    mat1[2][1] = 128;
    mat1[2][2] = 256;

    // Matrix 2
    int **mat2 = new int *[r2];
    for (int i = 0; i < r2; i++)
    {
        mat2[i] = new int[c2];
    }
    mat2[0][0] = 3;
    mat2[0][1] = 5;

    mat2[1][0] = 7;
    mat2[1][1] = 9;

    mat2[2][0] = 11;
    mat2[2][1] = 13;

    printProduct(mat1, mat2, r1, c1, r2, c2);
}

int main()
{
    std::cout << "Matrix Multiplication Classwork\n"
              << "Exercise 1: " << std::endl;
    exercise1(2, 2, 2, 4);

    std::cout << "\nExercise 2: " << std::endl;
    exercise2(3, 3, 3, 2);

    return 0;
}