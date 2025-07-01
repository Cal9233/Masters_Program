import random
import math

def guess():
    return random.randint(2, 5000)

def isPrime(n):
    """
    Checks if a given number 'n' is a prime number.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if 'n' is prime, False otherwise.
    """
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n == 2:
        return True   # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Other even numbers are not prime

    # Check for divisibility by odd numbers from 3 up to the square root of n
    # We only need to check up to the square root because if a number 'n' has a factor
    # greater than its square root, it must also have a factor smaller than its square root.
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False  # Found a divisor, so n is not prime
    return True  # No divisors found, so n is prime

def findPrimes(num):
    primes = []
    for i in range(num):
        p = guess()
        while not isPrime(p):
            p = guess()
        primes += [p]
    return primes

import cProfile
cProfile.run('print(findPrimes(500)[:10])')