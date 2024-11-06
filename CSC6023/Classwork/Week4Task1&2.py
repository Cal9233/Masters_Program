from math import ceil

def egyptian(n, d):
    print(f"\nThe Egyptian Fraction of {n}/{d} is:")
    ans = []
    # while numerator is not 0
    while (n > 0):
        x = ceil(d / n)          # compute the minimal larger denominator
        ans.append(x)            # hold it to the numerator list
        n, d = x * n - d, d * x  # update the remainder to n and d
    
    # Print the fraction expansion
    print(" + ".join([f"1/{a}" for a in ans]))
    return ans

def analyze_fraction(n, d, result):
    """Helper function to analyze and provide remarks about the solution"""
    print("\nRemarks:")
    print(f"- Number of unit fractions: {len(result)}")
    print(f"- Largest denominator: {max(result)}")
    print(f"- Smallest denominator: {min(result)}")
    print("-" * 50)

# Test cases
test_cases = [
    (5, 6),    # Case 1: 5/6
    (7, 15),   # Case 2: 7/15
    (23, 34),  # Case 3: 23/34
    (121, 321), # Case 4: 121/321
    (5, 123)   # Case 5: 5/123
]

print("Egyptian Fractions - Test Cases and Analysis")
print("=" * 50)

for numerator, denominator in test_cases:
    result = egyptian(numerator, denominator)
    analyze_fraction(numerator, denominator, result)

"""
Remarks about each case:

1. 5/6:
   - This is a relatively simple fraction
   - Converts to 1/2 + 1/3
   - Very efficient decomposition with small denominators

2. 7/15:
   - Slightly more complex than 5/6
   - Results in 1/3 + 1/5 + 1/15
   - Demonstrates how the algorithm handles odd numerators

3. 23/34:
   - A more complex fraction with larger numbers
   - Shows how the algorithm handles fractions close to 1
   - Results in multiple unit fractions

4. 121/321:
   - Large numbers test case
   - Shows how the algorithm handles more complex ratios
   - Results in several unit fractions
   - Demonstrates efficiency with larger numbers

5. 5/123:
   - Small numerator with large denominator
   - Shows how the algorithm handles disproportionate ratios
   - Results in larger denominators in the expansion
"""

"""
Analysis of why it doesn't work as intended:

Problem Identification:


The algorithm enters a situation where the values of n and d grow very large
The numerator never reaches 0, which is our termination condition
This leads to an infinite loop in the original code


Mathematical Analysis:


For 5/121, the first step calculates ceil(121/5) = 25
This gives us 1/25 as our first unit fraction
The new fraction becomes (255 - 121)/(12125)
This leads to 4/3025
The numbers continue to grow larger instead of reducing to 0


Root Cause:


The greedy algorithm assumes that each step will make progress toward reducing the remaining fraction to 0
In this case, the arithmetic operations result in a pattern that doesn't converge
The denominator grows much faster than the numerator reduces


Suggested Fixes:
a) Add a maximum iteration limit to prevent infinite loops
b) Consider alternative approaches for handling certain fraction patterns
c) Implement a check for growing denominators
d) Add validation for cases where the algorithm may not converge

To make this work properly, we would need to either:

Modify the algorithm to handle these special cases
Implement a different approach for fractions that follow this pattern
Add early detection of non-converging cases
"""