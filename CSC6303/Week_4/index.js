// Main Prime Checking Logic
function isPrimeNumber(n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 === 0 || n % 3 === 0) return false;
    
    for (let i = 5; i * i <= n; i += 6) {
    if (n % i === 0 || n % (i + 2) === 0) {
        return false;
    }
    }
    return true;
}

function isPrime() {
    const input = document.getElementById("nbr");
    const output = document.getElementById("outputAnswer");
    const number = parseInt(input.value);
    
    // Clear previous styling
    output.className = "";
    
    // Validate input
    if (isNaN(number) || input.value === "") {
    output.textContent = "Please enter a valid number.";
    output.className = "error";
    return;
    }
    
    if (number < 2 || number > 9999) {
    output.textContent = "Please enter a number between 2 and 9999.";
    output.className = "error";
    return;
    }
    
    // Check if prime
    if (isPrimeNumber(number)) {
    output.textContent = `${number} is a prime number.`;
    output.className = "prime";
    } else {
    output.textContent = `${number} is not a prime number.`;
    output.className = "not-prime";
    }
}

// Allow Enter key to submit
function handleKeyPress(event) {
    if (event.key === "Enter") {
    isPrime();
    }
}

// Initialize when page loads
window.onload = function() {
    document.getElementById("nbr").addEventListener("keypress", handleKeyPress);
    document.getElementById("nbr").focus();
};