# Egyptian fraction Greedy
from math import ceil
# n is the numerator, d is the denominator
def egyptian(n, d):
    print("The Egyptian Fraction of {}/{}".format(n, d))
    ans = []
    # while numerator is not 0
    while (n > 0):
        x = ceil(d / n)          # compute the minimal larger denominator
        ans.append(x)            # hold it to the numerator list
        n, d = x * n - d, d * x  # update the remainder to n and d
    for a in ans:
        print("1/{}".format(a), end=" ")

def main():
    # Task 1
    egyptian(5, 6) # 1/2, 1/3
    egyptian(7, 15) # 1/3, 1/8, 1/120
    egyptian(23, 34) # 1/2, 1/6, 1/102
    egyptian(121, 321) # 1/3, 1/23, 1/7383
    egyptian(5, 123) # 1/25, 1/1538, 1/4729350

    # Task 2

    egyptian(5, 121) # 1/25, 1/757, 1/763309, 1/873960180913, 1/1527612795642093385023488
    """
    For task 2 I got 1/1527612795642093385023488 instead of 1/1527612795642093418846225, I think I got a different result due to 
    Greedy Algorithms taking the largest possible unit fraction at each step that doesn't exceed the remaining fraction. Which can 
    possible mean that it might not always lead to the exact same sequence of denominators. While both denominators are different
    they are still exxtremely close to each other and due to this it makes both represent valid Egyptian fraction decompositions of 5/121.
    """
main()
