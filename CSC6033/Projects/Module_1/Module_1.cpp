#include <iostream>
using namespace std;

int dotProduct(int *v1, int *v2, int nums)
{
    int result = 0;

    for (int i = 0; i < nums; i++)
    {
        result += v1[i] * v2[i];
    }

    return result;
}

int main()
{
    std::cout << "Calvin Malagon Module 1 Project \n"
              << std::endl;

    int *vector1 = new int[3];
    vector1[0] = 8;
    vector1[1] = 16;
    vector1[2] = 32;

    int *vector2 = new int[3];
    vector2[0] = 5;
    vector2[1] = 9;
    vector2[2] = 13;

    int result = dotProduct(vector1, vector2, 3);
    std::cout << "Result: " << result << endl;

    delete[] vector1;
    delete[] vector2;
    return 0;
}