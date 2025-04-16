// Write a function throttle(fn, delay) that returns a throttled version of the input function. 
// The throttled function, when called repeatedly, should only invoke the original function at most once per delay milliseconds.

// Throttle is a technique used to limit the rate of function execution.
// It ensures that a function is called at most once within a specified time interval, 
// regardless of how many times the triggering event occurs.

function throttle(fn, delay){
    let timeoutId;
    let lastExecTime = 0;
    return (...args) => {
        const currentTime = Date.now();
        const timeSinceLastExec = currentTime - lastExecTime;
        if(!timeoutId){
            if(timeSinceLastExec >= delay){
                fn.apply(this, args);
                lastExecTime = currentTime;
            } else {
                timeoutId = setTimeout(() => {
                    fn.apply(this, args);
                    lastExecTime = Date.now();
                    timeoutId = null;
                }, delay - timeSinceLastExec)
            }
        }
    }
}

// Test function
function testThrottle() {
    // Create a counter to track function calls
    let counter = 0;
    
    // Function to be throttled
    function incrementCounter() {
      counter++;
      console.log(`Function called! Counter: ${counter}, Time: ${new Date().toLocaleTimeString()}`);
    }
    
    // Create throttled version - only allow calls every 1000ms (1 second)
    const throttledIncrement = throttle(incrementCounter, 1000);
    
    // Set up an interval that tries to call the function every 100ms
    const intervalId = setInterval(() => {
      console.log("Attempting to call function...");
      throttledIncrement();
    }, 100);
    
    // Stop the test after 3 seconds
    setTimeout(() => {
      clearInterval(intervalId);
      console.log(`Test complete. Function was called ${counter} times.`);
      // Should be approximately 3-4 times depending on exact timing
    }, 3000);
  }
  
  // Run the test
  testThrottle();