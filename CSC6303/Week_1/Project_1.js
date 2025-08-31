/**
 * Factorial Calculator Program
 * 
 * This program calculates the factorial of a user-provided positive integer.
 * The factorial of a non-negative integer n is the product of all positive 
 * integers less than or equal to n (n! = n × (n-1) × (n-2) × ... × 1).
 * By mathematical convention, 0! = 1.
 * 
 * @author Calvin Malagon
 * @version 1.0
 * @since 2025
 */

const readline = require('readline');

// Create readline interface for handling user input/output
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

/**
 * Main factorial calculation function that handles user interaction
 * and input validation through a nested helper function.
 * 
 * This function orchestrates the entire factorial calculation process:
 * 1. Prompts user for input
 * 2. Validates the input
 * 3. Calculates factorial if valid
 * 4. Re-prompts if invalid
 * 
 * @function fact
 * @returns {void} No return value - outputs result to console
 */
function fact() {
    /**
     * Nested helper function that handles user prompting and input validation.
     * Uses recursion to re-prompt user until valid input is received.
     * 
     * @function promptUser
     * @param {string} [message="Enter an positive Integer: "] - The prompt message to display
     * @returns {void} No return value - processes input and calls factorial calculation
     */
    function promptUser(message = "Enter an positive Integer: ") {
        // Display prompt and wait for user input
        rl.question(message, (input) => {
            /**
             * Convert user input string to integer
             */
            let n = parseInt(input);
            
            /**
             * Input validation block
             * Checks for two invalid conditions
             * 
             * If either condition is true, recursively call promptUser 
             * with error message to re-prompt the user.
             */
            if (isNaN(n) || n < 0) {
                // Recursive call with error message for invalid input
                promptUser("Sorry, only positive numbers, enter again: ");
            } else {
                //Valid input received - proceed with factorial calculation
                
                // Special case: 0! = 1 (mathematical convention)
                if (n === 0) {
                    console.log("The factorial of 0 is 1");
                } else {
                    /**
                     * @variable {number} f - Accumulator for factorial result, starts at 1
                     * @variable {number} i - Loop counter from 1 to n (inclusive)
                     */
                    let f = 1; // Initialize factorial result to 1
                    
                    // Iterative multiplication loop
                    for (let i = 1; i <= n; i++) {
                        f *= i;
                    }
                    
                    // Display the calculated factorial result
                    console.log("The factorial of", n, "is", f);
                }
                
                /**
                 * Close the readline interface to end the program
                 * This prevents the program from hanging and allows clean exit
                 */
                rl.close();
            }
        });
    }
    
    // Start the interaction by calling promptUser with default message
    promptUser();
}

// Execute the main factorial function to start the program
fact();