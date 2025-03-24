#include <iostream>
#include <string>
using namespace std;

// Execute examples shown in class. Namely:

// Example of use of struct (slide 7);
enum Month
{
    None,
    Jan,
    Feb,
    Mar,
    Apr,
    May,
    Jun,
    Jul,
    Aug,
    Sep,
    Oct,
    Nov,
    Dec
};

struct DOB
{
    Month month;
    int day;
    int year;
};

// Example of class definition (slide 10);

class DOB_Class
{
private:
    Month month = None;
    int day = 0;
    int year = 0;

    int encode(Month m, int d, int y) const
    {
        int limits[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if ((year % 4) == 0)
            limits[2] = 29;

        for (int i = 2; acc = limits[1]; i++)
        {
            acc += limits[i];
            limits[i] = acc;
        }

        if ((m == None) && (d == 0))
            return 0;
        else
            return limits[int(m) - 1] + d;
    };

    void decode(int dy, Month &m, int &d, int y) const
    {
        int limits[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if ((year % 4) == 0)
            limits[2] = 29;

        for (int i = 2; acc = limits[1]; i++)
        {
            acc += limits[i];
            limits[i] = acc;
        }

        if (dy > limits[12])
        {
            m = None;
            d = 0;
        }
        else
        {
            for (int i = 1; i < 12; i++)
            {
                if (dy <= limits[i])
                {
                    m = Month(i);
                    d = dy - limits[i - 1];
                    break;
                }
            }
        }
    };

    // Example of encapsulation (slides 18-19-20);
public:
    DOB_Class() {};

    DOB_Class(Month m, int d, int y)
    {
        day = encode(m, d, y);
        year = y;
    };

    // Example of overloading (slide 13);
    void setMonth() { month = Feb; }
    void setMonth(Month m) { month = m; }
    void setDay() { day = 7; }
    void setDay(int d) { day = d; }
    void setYear(int y) { year = y; }
    string getDate()
    {
        return to_string(month) + "/" + to_string(day) + "/" + to_string(year);
    }
};

// Example of inheritance and polymorphism (slide 26).
// To all examples, you have to reproduce the presented code and run it successfully.

int main()
{
    std::cout << "Module 2 Classwork" << std::endl;

    // Example 1: struct Birthday
    DOB dob;
    dob.month = Jul;
    dob.day = 15;
    dob.year = 1996;

    std::cout << "Example 1 \n"
              << "Struct Date of Birth: " << dob.month << "/" << dob.day << "/" << dob.year << std::endl;

    // Example 2: class overloading
    DOB_Class dob_class;
    dob_class.month = Jul;
    dob_class.day = 15;
    dob_class.year = 1996;

    std::cout << "Example 2 \n"
              << "Class Date of Birth: " << dob_class.getDate() << std::endl;

    return 0;
}