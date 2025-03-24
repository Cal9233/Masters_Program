#include <iostream>
using namespace std;

class squareMatrix
{
private:
    double **bi_arr;

public:
    int order_size;

    // Initialize allocated matrix
    squareMatrix(int n)
    {
        order_size = n;

        bi_arr = new double *[n];

        for (int i = 0; i < n; i++)
        {
            bi_arr[i] = new double[n];
            for (int j = 0; j < n; j++)
            {
                bi_arr[i][j] = 0;
            }
        }
    };

    // Delete allocated matrix to prevent memory leaks
    ~squareMatrix()
    {
        for (int i = 0; i < order_size; i++)
        {
            delete[] bi_arr[i];
        }
        delete[] bi_arr;
    }

    // Getter method delivering element
    double getRowCol(int row, int col)
    {
        if (row < order_size && row >= 0 && col >= 0 && col < order_size)
        {
            return bi_arr[row][col];
        }
        // Edge case
        else
        {
            std::cout << "Index out of bounds" << std::endl;
            return -1;
        }
    };

    // Setter method inputting value
    void setRowCol(int row, int col, double value)
    {
        if (row < order_size && row >= 0 && col >= 0 && col < order_size)
        {
            bi_arr[row][col] = value;
        }
        // Edge case
        else
        {
            std::cout << "Index out of bounds" << std::endl;
            return;
        }
    }

    // Getter method delivering single dimension vector of diagonal elements
    double *getDiagonal()
    {
        double *diagonal = new double[order_size];
        // Edge case
        if (order_size == 0)
        {
            std::cout << "Square Matrix is empty" << std::endl;
        }
        else
        {
            for (int i = 0; i < order_size; i++)
            {
                diagonal[i] = bi_arr[i][i];
            }
        }
        return diagonal;
    }
};

int main()
{
    std::cout << "Calvin Malagon Project 2" << "\n"
              << std::endl;

    // Allocating 2D Square Matrix
    squareMatrix sm(3);
    std::cout << "Initializing Matrix:"
              << std::endl;

    // Setting values for matrix
    sm.setRowCol(0, 0, 1.5);
    sm.setRowCol(0, 1, 2.0);
    sm.setRowCol(0, 2, 3.3);
    sm.setRowCol(1, 0, 4.1);
    sm.setRowCol(1, 1, 5.7);
    sm.setRowCol(1, 2, 6.2);
    sm.setRowCol(2, 0, 7.4);
    sm.setRowCol(2, 1, 8.9);
    sm.setRowCol(2, 2, 9.0);

    // Getting values for matrix
    std::cout << "Get [1, 2] value:"
              << std::endl;
    std::cout << sm.getRowCol(1, 2) << "\n"
              << std::endl;
    std::cout << "Get [2, 2] value:"
              << std::endl;
    std::cout << sm.getRowCol(2, 2) << "\n"
              << std::endl;
    std::cout << "Diagonal Method:"
              << std::endl;

    // Displaying diagonal values of Matrix
    double *diagonal = sm.getDiagonal();
    std::cout << "[";
    for (int i = 0; i < sm.order_size; i++)
    {
        std::cout << "[";
        std::cout << diagonal[i];
        if (i == sm.order_size - 1)
            std::cout << "]";
        else
            std::cout << "],";
    }
    std::cout << "]" << std::endl;

    // Preventing memory leak
    delete[] diagonal;
    return 0;
}