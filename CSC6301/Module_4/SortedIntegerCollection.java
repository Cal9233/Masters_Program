package CSC6301.Module_4;

import java.util.*;

/**
 * Manages a sorted collection of integers using LinkedList.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 4 of CSC6301
 */
public class SortedIntegerCollection implements SortedCollection {

    /** LinkedList storing integers in sorted order */
    private final LinkedList<Integer> numbers;

    /**
     * Constructor initializes the LinkedList.
     * Demonstrates code reuse through Collections Framework.
     */
    public SortedIntegerCollection() {
        this.numbers = new LinkedList<>();
    }

    /**
     * Adds a number maintaining sorted order using binary search.
     * 
     * EXPLICIT REUSE: This method demonstrates strategic REUSE by leveraging
     * Collections.binarySearch() rather than implementing our own search algorithm.
     * 
     * REUSED COMPONENTS: Collections.binarySearch() method, built-in comparison
     * logic
     * NOT REIMPLEMENTED: Binary search algorithm, array bounds handling, insertion
     * point calculation for negative indices
     * 
     * The Java implementation we REUSE provides optimized performance and handles
     * edge cases like duplicate values automatically. If we had avoided this REUSE
     * and written from scratch, we would need to implement the binary search logic,
     * handle array bounds, and manage insertion point calculations - all of which
     * are already thoroughly tested in the Collections framework.
     * 
     * @param number the integer to add
     */
    @Override
    public void add(Integer number) {
        int insertionIndex = Collections.binarySearch(numbers, number);

        if (insertionIndex < 0) {
            insertionIndex = -(insertionIndex + 1);
        }

        numbers.add(insertionIndex, number);
    }

    /**
     * Returns all numbers in sorted order.
     * Demonstrates code reuse through defensive copying pattern.
     * 
     * @return new LinkedList containing the sorted numbers
     */
    @Override
    public List<Integer> getNumbers() {
        return new LinkedList<>(numbers);
    }
}