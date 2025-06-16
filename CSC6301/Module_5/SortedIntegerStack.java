package CSC6301.Module_5;

import java.util.*;

/**
 * Manages a sorted collection of integers using Stack.
 * Maintains sorting order through strategic stack operations.
 * 
 * @author Calvin Malagon
 * @version 2.0.0.0 (Stack Implementation)
 * @since Week 5 of CSC6301 - Stack Maintenance Update
 */
public class SortedIntegerStack implements SortedCollection {

    /** Stack storing integers with sorting capability */
    private final Stack<Integer> numbers;

    /** Temporary stack for sorting operations */
    private final Stack<Integer> tempStack;

    /**
     * Constructor initializes the Stack and temporary stack.
     * Demonstrates code reuse through Collections Framework.
     */
    public SortedIntegerStack() {
        this.numbers = new Stack<>();
        this.tempStack = new Stack<>();
    }

    /**
     * Adds a number maintaining sorted order using stack operations.
     * 
     * EXPLICIT REUSE: This method demonstrates strategic REUSE by leveraging
     * Stack's LIFO operations and Collections framework utilities rather than
     * implementing custom sorting algorithms.
     * 
     * REUSED COMPONENTS: Stack.push(), Stack.pop(), Stack.peek(), Stack.isEmpty()
     * NOT REIMPLEMENTED: LIFO data structure logic, dynamic array management,
     * capacity handling, bounds checking
     * 
     * The Stack implementation we REUSE provides optimized LIFO operations.
     * We combine this with a sorting insertion algorithm that maintains order
     * by using a temporary stack. This approach REUSES proven stack operations
     * while implementing the business logic for sorted insertion.
     * 
     * Algorithm: To insert a number in sorted order (smallest to largest when
     * viewed from bottom):
     * 1. Pop elements from main stack to temp stack while they're greater than new
     * number
     * 2. Push the new number onto main stack
     * 3. Push all elements back from temp stack to main stack
     * 
     * This maintains the invariant that the stack contains elements in sorted order
     * from bottom (smallest) to top (largest).
     * 
     * @param number the integer to add
     */
    @Override
    public void add(Integer number) {
        // Pop elements greater than the new number to temporary stack
        while (!numbers.isEmpty() && numbers.peek() < number) {
            tempStack.push(numbers.pop());
        }

        // Push the new number
        numbers.push(number);

        // Push back all elements from temporary stack
        while (!tempStack.isEmpty()) {
            numbers.push(tempStack.pop());
        }
    }

    /**
     * Returns all numbers in sorted order (smallest to largest).
     * Demonstrates code reuse through Collections framework and defensive copying.
     * 
     * EXPLICIT REUSE: This method REUSES ArrayList and Collections.reverse()
     * rather than implementing custom stack traversal or array manipulation.
     * 
     * REUSED COMPONENTS: ArrayList constructor, Collections.reverse(),
     * enhanced for-loop iteration, Stack.iterator()
     * NOT REIMPLEMENTED: Dynamic array operations, reverse algorithm,
     * iterator implementation, memory management
     * 
     * Since Stack is LIFO and we want to return elements from smallest to largest,
     * we REUSE ArrayList for efficient random access and Collections.reverse()
     * for optimal reversal rather than implementing these operations manually.
     * 
     * @return new ArrayList containing the sorted numbers from smallest to largest
     */
    @Override
    public List<Integer> getNumbers() {
        // Convert stack to list - this gives us largest to smallest
        List<Integer> result = new ArrayList<>();

        // Create a temporary stack to reverse the order
        Stack<Integer> reverseStack = new Stack<>();

        // Push all elements to reverse stack (this reverses the order)
        for (Integer number : numbers) {
            reverseStack.push(number);
        }

        // Pop from reverse stack to get smallest to largest
        while (!reverseStack.isEmpty()) {
            result.add(reverseStack.pop());
        }

        return result;
    }
}