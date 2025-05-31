#include <iostream>
#include <string>

int main()
{
    std::string str;
    int count = 0;
    char buffer[1000];
    std::cout << "Enter a string: ";
    std::cin >> str;
    for (char c : str)
    {
        if (c == 'b')
            count++;
    }
    std::string binary = "";
    while (count > 0)
    {
        binary = std::to_string(count % 2) + binary;
        count /= 2;
    }
    std::cout << binary << std::endl;
    return 0;
}