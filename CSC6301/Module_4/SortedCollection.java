package CSC6301.Module_4;


import java.util.List;

/**
 * Interface for sorted collection operations.
 * Follows Interface Segregation Principle by defining only essential
 * operations.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 4 of CSC6301
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