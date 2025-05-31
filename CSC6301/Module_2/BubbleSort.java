import java.util.Arrays;

/**
 * BubbleSort class
 * 
 * Class that performs Bubble Sort Algorithm to a static list of numbers.
 * Bubble sort works by repeatedly comparing adjacent elements and swapping them
 * if they are in the wrong order, until the entire array is sorted.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 2 of CSC6301
 */
public class BubbleSort {
    /**
     * Sorts an array of integers using the Bubble Sort algorithm.
     * The algorithm compares adjacent elements and swaps them if they're in the
     * wrong order.
     * This process is repeated until the array is sorted in ascending order.
     * 
     * @param array the integer array to be sorted
     */
    static void bubbleSort(int array[]) {
        int size = array.length;
        // Loops through array of integers
        for (int i = 0; i < (size - 1); i++) {
            boolean swapped = false;
            for (int j = 0; j < (size - i - 1); j++) {
                // Compare adjacent elements and swap if necessary
                if (array[j] > array[j + 1]) {
                    // Swap elements using temporary variable
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                    swapped = true;
                }
            }
            // If no swapping occurred in this pass, array is sorted
            if (!swapped)
                break;
        }
    }

    /**
     * Main method that demonstrates the bubble sort algorithm.
     * Creates a sample integer array, sorts it using bubbleSort method,
     * and displays the sorted result.
     * 
     * @param args command line arguments (not used)
     */
    public static void main(String args[]) {
        // Sample array to be sorted
        int[] data = { 2, 45, 37, 21, 31, 50, 29, 22, 67, 88, 56 };
        // Call bubble sort method to sort the array
        BubbleSort.bubbleSort(data);
        // Output the sorted array
        System.out.println("Sorted Array in Ascending Order.");
        System.out.println(Arrays.toString(data));
    }
}