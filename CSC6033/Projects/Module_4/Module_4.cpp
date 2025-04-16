#include <iostream>
using namespace std;

enum states
{
    START,
    A_ACCEPT,
    A_CONTINUE,
    B1,
    B2_ACCEPT,
    B_CONTINUE,
    REJECT
};

class FSA
{
private:
    states current_state;

public:
    FSA()
    {
        current_state = START;
    }

    void charProcess(char c)
    {

        switch (current_state)
        {
        case START:
            if (c == 'a')
                current_state = A_ACCEPT;
            else if (c == 'b')
                current_state = B1;
            else
                current_state = START;
            break;

        case A_ACCEPT:
        case A_CONTINUE:
            if (c == 'a' || c == 'b')
                current_state = A_CONTINUE;
            else
                current_state = REJECT;
            break;

        case B1:
            if (c == 'b')
                current_state = B2_ACCEPT;
            else
                current_state = REJECT;
            break;

        case B2_ACCEPT:
        case B_CONTINUE:
            if (c == 'a')
                current_state = B_CONTINUE;
            else
                current_state = REJECT;
            break;

        case REJECT:
            break;
        }
    }

    bool isAccepted(string input)
    {
        current_state = START;
        int strLength = input.length();
        for (int i = 0; i < strLength; i++)
        {
            charProcess(input[i]);
            if (current_state == REJECT)
                return false;
        }
        return (current_state == A_ACCEPT || current_state == A_CONTINUE || current_state == B_CONTINUE || current_state == B2_ACCEPT);
    }
    void wordResult(string input)
    {
        if (input.empty())
        {
            std::cout << "Word \"" << input << "\" is invalid (empty string)." << std::endl;
            return;
        }

        if (isAccepted(input))
        {
            std::cout << "Word \"" << input << "\" is valid." << std::endl;
        }
        else
        {
            std::cout << "Word \"" << input << "\" is invalid." << std::endl;
        }
    }
};

// Create also a main function that receives a string to be analyzed and delivers the result computed by the FSA
int main()
{
    // Start State is Invalid until proven otherwise
    std::cout << "Calvin Malagon Module 4 Project" << std::endl;
    FSA fsa;
    string userInput;
    cout << "\nEnter a word to check (or 'exit' to quit): ";
    // Use getline instead of cin >> to properly handle empty input
    while (getline(cin, userInput) && userInput != "exit")
    {
        fsa.wordResult(userInput);
        cout << "Enter a word to check (or 'exit' to quit): ";
    }
    return 0;
}