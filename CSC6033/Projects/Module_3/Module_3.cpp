#include <iostream>
#include <string>
using namespace std;

// The class should have at least:
// The enum for the states,
enum states
{
    START,
    ACCEPT,
    A1,
    B1,
    C1,
    A2,
    B2,
    A3,
    B3
};

class FSA
{
private:
    states current_state;
    int len;

public:
    FSA()
    {
        current_state = START;
        len = 0;
    }

    // A method for processing the chars,
    void charProcess(char c)
    {
        len++; // Increment length counter

        switch (current_state)
        {
        case START:
            if (c == 'a')
                current_state = A1;
            else if (c == 'b')
                current_state = B1;
            else
                current_state = START; // On 'c', stay at start
            break;

        case A1:
            if (c == 'a')
                current_state = A2;
            else if (c == 'b')
                current_state = B1;
            else
                current_state = START; // On 'c', go back to start
            break;

        case A2:
            if (c == 'a')
                current_state = A3;
            else if (c == 'b')
                current_state = B1;
            else
                current_state = START;
            break;

        case A3: // Already accepted, stay in accepting state
            current_state = ACCEPT;
            break;

        case B1:
            if (c == 'a')
                current_state = A1;
            else if (c == 'b')
                current_state = B2;
            else
                current_state = START;
            break;

        case B2:
            if (c == 'a')
                current_state = A1;
            else if (c == 'b')
                current_state = B3;
            else
                current_state = START;
            break;

        case B3: // Already accepted, stay in accepting state
            current_state = ACCEPT;
            break;

        case C1:
            if (c == 'a')
                current_state = A1;
            else if (c == 'b')
                current_state = B1;
            else
                current_state = START;
            break;

        case ACCEPT: // Once accepted, stay accepted
            break;
        }
    }

    // A method for deciding if the word is accepted or rejected.
    bool wordProcess(string input)
    {
        current_state = START;
        len = 0;
        int strLength = input.length();
        for (int i = 0; i < strLength; i++)
        {
            charProcess(input[i]);
        }
        return (len >= 3) && (current_state == A3 || current_state == B3 || current_state == ACCEPT);
    }
    void wordResult(string input)
    {
        // This part checks for empty strings:
        if (input.empty())
        {
            std::cout << "Word \"" << input << "\" is invalid (empty string)." << std::endl;
            return;
        }

        if (wordProcess(input))
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
    std::cout << "Calvin Malagon Module 3 Project" << std::endl;
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