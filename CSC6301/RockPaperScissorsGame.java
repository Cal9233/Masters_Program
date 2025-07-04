import java.util.Scanner;
import java.util.Random;

/**
 * Rock Paper Scissors Game implementation following Java best practices.
 * 
 * This class provides functionality to play a single round of Rock Paper
 * Scissors against the computer.
 * 
 * The user selects rock, paper, or scissors, and the computer randomly selects
 * one as well.
 * The result of the match is determined based on standard game rules.
 * 
 * @author Calvin Malagon
 * @version 1.0.0
 * @since 1.0.0
 */
public class RockPaperScissorsGame {

    private static final String ROCK = "r";
    private static final String SCISSORS = "s";
    private static final String PAPER = "p";

    private Scanner inputScanner;
    private Random randomGenerator;

    /**
     * Constructs a new RockPaperScissorsGame instance.
     * 
     * Initializes the input scanner and random number generator used for
     * gameplay.
     */
    public RockPaperScissorsGame() {
        this.inputScanner = new Scanner(System.in);
        this.randomGenerator = new Random();
    }

    /**
     * Starts and manages a single round of the Rock Paper Scissors game.
     * 
     * Handles user input, generates the computer's move, determines the outcome,
     * displays the result, and closes input resources.
     */
    public void playRockPaperScissors() {
        String playerGuess = "";

        // Get valid user input
        while (true) {
            System.out.print("Enter (r)ock, (s)cissors, or (p)aper: ");
            playerGuess = inputScanner.nextLine().toLowerCase().trim();

            if (!isValidChoice(playerGuess)) {
                System.out.println("Only 'r', 's', or 'p' are valid inputs! Please try again.");
            } else {
                break;
            }
        }

        // Generate computer choice
        String computerChoice = generateComputerChoice();

        // Determine and display result
        determineAndDisplayResult(playerGuess, computerChoice);

        // Clean up resources
        closeResources();
    }

    /**
     * Checks if the player's input is a valid game option.
     * 
     * @param choice The player's input
     * @return true if input is "r", "s", or "p"; false otherwise
     */
    private boolean isValidChoice(String choice) {
        return ROCK.equals(choice) || SCISSORS.equals(choice) || PAPER.equals(choice);
    }

    /**
     * Randomly selects the computer's move.
     * 
     * Each of the three choices—rock, paper, or scissors—has equal probability.
     * 
     * @return The computer's move as a single-letter string
     */
    private String generateComputerChoice() {
        double randomValue = randomGenerator.nextDouble();

        if (randomValue < 1.0 / 3.0) {
            return ROCK;
        } else if (randomValue < 2.0 / 3.0) {
            return SCISSORS;
        } else {
            return PAPER;
        }
    }

    /**
     * Compares the player's and computer's choices and prints the outcome.
     * 
     * Displays whether the result is a win, loss, or tie.
     * 
     * @param playerChoice   The player's move
     * @param computerChoice The computer's move
     */
    private void determineAndDisplayResult(String playerChoice, String computerChoice) {
        if (playerChoice.equals(computerChoice)) {
            System.out.println("It is a tie!");
        } else if (playerLoses(playerChoice, computerChoice)) {
            System.out.println("Sorry, you lost as I had " + computerChoice);
        } else {
            System.out.println("Congrats, you won as I had " + computerChoice);
        }
    }

    /**
     * Determines if the player loses based on standard game rules.
     * 
     * @param playerChoice   The player's move
     * @param computerChoice The computer's move
     * @return true if the player loses; false otherwise
     */
    private boolean playerLoses(String playerChoice, String computerChoice) {
        return (ROCK.equals(playerChoice) && PAPER.equals(computerChoice)) ||
                (PAPER.equals(playerChoice) && SCISSORS.equals(computerChoice)) ||
                (SCISSORS.equals(playerChoice) && ROCK.equals(computerChoice));
    }

    /**
     * Releases input-related system resources.
     * 
     * Should be called after the game ends to properly close the scanner.
     */
    private void closeResources() {
        if (inputScanner != null) {
            inputScanner.close();
        }
    }

    /**
     * Main method to launch the Rock Paper Scissors game.
     * 
     * @param args Command line arguments
     */
    public static void main(String[] args) {
        RockPaperScissorsGame game = new RockPaperScissorsGame();
        game.playRockPaperScissors();
    }
}
