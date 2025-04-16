#include <iostream>
#include <string>
#include <stack>

bool isStringValid(const std::string &input)
{
    std::stack<char> charStack;

    for (char c : input)
    {
        // Skip valid characters
        if ((c >= 'a' && c <= 'z') || c == ' ')
        {
            continue;
        }

        // Push to stack if open bracket/paranthesis
        if (c == '(' || c == '[')
        {
            charStack.push(c);
        }
        // If it's a closing bracket/parenthesis
        else if (c == ')' || c == ']')
        {
            // If stack is empty, there's no matching opening bracket
            if (charStack.empty())
            {
                return false;
            }

            // Get top element
            char top = charStack.top();

            // Check if they match
            if ((c == ')' && top != '(') || (c == ']' && top != '['))
            {
                return false;
            }

            // Remove the matched opening bracket from stack
            charStack.pop();
        }
        // If character is not in the alphabet
        else
        {
            std::cout << "Error: Character '" << c << "' not in alphabet." << std::endl;
            return false;
        }
    }

    // Empty stack means string is valid
    return charStack.empty();
}

int main()
{
    std::string input;
    std::cout << "Please enter a string thats in the alphabet (Σ = { a-z, ␢, (, ), [, ] }): ";
    std::getline(std::cin, input);

    // Checks to see if user input is in alphabet
    for (char c : input)
    {
        if (!((c >= 'a' && c <= 'z') || c == ' ' || c == '(' || c == ')' || c == '[' || c == ']'))
        {
            std::cout << "Error: Character '" << c << "' not in alphabet." << std::endl;
            return -1;
        }
    }

    // Analyze users input
    bool result = isStringValid(input);

    if (result)
    {
        std::cout << "User string is valid." << std::endl;
    }
    else
    {
        std::cout << "User string is invalid." << std::endl;
    }

    return 0;
}