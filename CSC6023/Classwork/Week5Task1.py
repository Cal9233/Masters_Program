from random import randrange

def test(initialSize, probRemove):
    accCheap, accCosty = 0, 0
    s = initialSize
    m = 2*s
    for i in range(100000):
        if (randrange(100) < probRemove):
            if (s > 0):
                s -= 1
        else:
            if (s == m):
                m = m*2
                s += 1
                accCosty += 1
            else:
                s += 1
                accCheap += 1
    print("Initial size:", initialSize, "Prob Remove:", probRemove, "out of 100")
    print("Costy: {:7} ({:3.1}%)".format(accCosty,100*accCosty/(accCosty+accCheap)))
    print("Cheap: {:7} ({:3.1}%)".format(accCheap,100*accCheap/(accCosty+accCheap)))

def main():
    """
    Test cases demonstrating why costly operations percentage remains low
    We Use smallest possible initial size (1) to force early doublings. Then we
    minimize removals (probRemove = 0 or 1) to maintain growth. But even with these 
    optimal conditions, costly operations remain rare due to exponential growth pattern.
    
    This creates a pattern where each costly operation is preceded by
    increasingly more cheap operations, making it impossible to maintain
    a high percentage of costly operations over time.
    """
    test(10, 1)
    test(10, 5)
    test(20, 1)
    test(20, 5)
    test(50, 1)
    test(50, 5)
    test(100, 1)
    test(100, 5)
  # attempts
    test(1, 1)
    test(2, 1)
    test(3, 1)
    test(1, 0)
    """
    Why it's not possible to achieve 1% costly operations:
    
    1. The array doubles in size each time it's full, so if we start with size 1, 
    next expansions are at 2, 4, 8, 16, 32, ... , etc. Each doubling reduces future 
    costly operations exponentially.
    
    2. Even with minimal removal (probRemove = 1) the array will grow exponentially. So
    most operations will happen when the array is large and large arrays mean more cheap operations 
    between costly ones.
    
    3. If we have zero removal then we get the theoretical maximum of costly operations but 
    due to exponential growth, it's still hard to reach 1%.
    
    All of this demonstrates the key feature of dynamic arrays which is,
    their amortized cost analysis holds true (costly operations). Which
    becomes increasingly rare as the array grows, making them efficient for long-term use.
    """
main()
