package CSC6301.Module_5;

import java.util.List;

/**
 * Interface for sorted collection operations.
 * Follows Interface Segregation Principle by defining only essential
 * operations.
 * 
 * @author Calvin Malagon
 * @version 2.0.0.0 (Stack Implementation)
 * @since Week 5 of CSC6301 - Stack Maintenance Update
 */
public interface SortedCollection {

    /**
     * Adds a number to the collection maintaining sorted order.
     * 
     * @param number the integer to add to the collection
     */
    void add(Integer number);

    /**
     * Returns all numbers in sorted order.
     * 
     * @return list of all numbers in sorted order
     */
    List<Integer> getNumbers();
}