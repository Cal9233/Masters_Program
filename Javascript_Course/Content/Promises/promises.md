### Promise

A promise is an Object that contains asynchronous operations. Which is actually a state.
state -> pending, fulfilled, rejected

Promise.all takes in an array of promises and returns a new promise of the resolved promises from the array.
Waits for all of them to fetch.

Promose.race returns the promise that fetches first as the value.

Promise.any returns the first promise to fulfill.
