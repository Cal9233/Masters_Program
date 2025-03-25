#include <iostream>
#include <string>
using namespace std;

// Execute examples shown in class. Namely:

// Example of use of enum (for Month)
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

// Example of use of struct (slide 7)
struct DOB_Struct
{
    Month month;
    int day;
    int year;
};

// Example of class definition (slide 10)
class DOB
{
protected:
    Month month = None;
    int day = 0;
    int year = 0;

    int encode(Month m, int d, int y) const
    {
        int limits[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if ((y % 4) == 0)
            limits[2] = 29;

        int acc = limits[1];
        for (int i = 2; i <= 12; i++)
        {
            acc += limits[i];
            limits[i] = acc;
        }

        if ((m == None) && (d == 0))
            return 0;
        else
            return limits[int(m) - 1] + d;
    }

    void decode(int dy, Month &m, int &d, int y) const
    {
        int limits[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if ((y % 4) == 0)
            limits[2] = 29;

        int acc = limits[1];
        for (int i = 2; i <= 12; i++)
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
            for (int i = 1; i <= 12; i++)
            {
                if (dy <= limits[i])
                {
                    m = Month(i);
                    d = dy - limits[i - 1];
                    break;
                }
            }
        }
    }

    // Example of encapsulation (slides 18-19-20)
public:
    DOB() {}

    DOB(Month m, int d, int y)
    {
        month = m;
        day = d;
        year = y;
    }

    // Example of overloading (slide 13)
    void setMonth(Month m) { month = m; }
    void setDay(int d) { day = d; }
    void setYear(int y) { year = y; }

    Month getMonth() const { return month; }
    int getDay() const { return day; }
    int getYear() const { return year; }

    string getDate() const
    {
        string monthNames[13] = {"None", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
        return monthNames[int(month)] + "/" + to_string(day) + "/" + to_string(year);
    }
};

// Example of inheritance and polymorphism (slide 26)
class HOB : public DOB
{
private:
    int hour = 0;
    int mins = 0;

public:
    HOB() {}
    HOB(Month m, int d, int y, int h, int n) : DOB(m, d, y)
    {
        hour = h;
        mins = n;
    }

    void setHour(int h) { hour = h; }
    void setMinutes(int m) { mins = m; }

    // Override the base class method (polymorphism)
    string getDate() const
    {
        int h = (hour == 0) ? 12 : (hour < 13) ? hour
                                               : hour - 12;
        string ampm = (hour < 12) ? "AM" : "PM";

        string monthNames[13] = {"None", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};

        return monthNames[int(month)] + "/" + to_string(day) + "/" + to_string(year) +
               " " + to_string(h) + ":" + to_string(mins) + " " + ampm;
    }
};

int main()
{
    std::cout << "Calvin Malagon Module 2 Classwork" << std::endl;

    // Example 1: struct DOB_Struct
    DOB_Struct dob_struct;
    dob_struct.month = Jul;
    dob_struct.day = 15;
    dob_struct.year = 1996;

    std::cout << "Example 1 Struct \n"
              << "Struct Date of Birth: " << int(dob_struct.month) << "/"
              << dob_struct.day << "/" << dob_struct.year << std::endl;

    // Example 2: class usage
    DOB dob_class;
    dob_class.setMonth(Jul);
    dob_class.setDay(15);
    dob_class.setYear(1996);

    std::cout << "Example 2 Class \n"
              << "Class Date of Birth: " << dob_class.getDate() << std::endl;

    // Example 3: overloading (showing the use of overloaded methods)
    DOB dob_overload(Aug, 22, 2000);
    std::cout << "Example 3 Overloading \n"
              << "Class Date of Birth: " << dob_overload.getDate() << std::endl;

    // Example 4: encapsulation (showing the use of getters and setters)
    DOB dob_encap;
    dob_encap.setMonth(Sep);
    dob_encap.setDay(10);
    dob_encap.setYear(2010);
    std::cout << "Example 4 Encapsulation \n"
              << "Class Date of Birth: " << dob_encap.getDate() << std::endl;

    // Example 5: inheritance and polymorphism
    DOB dob_poly(Mar, 14, 2012);
    HOB hob(Feb, 23, 1998, 22, 30);
    std::cout << "Example 5 Inheritance and Polymorphism \n"
              << "DOB Class: " << dob_poly.getDate()
              << " - HOB Class: " << hob.getDate() << std::endl;

    return 0;
}