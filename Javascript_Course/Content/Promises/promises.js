const promise = Promise.resolve(3);

console.log(promise);

promise
.then(val => val * 2)
.then(val => val + 1)
.then(val => {
    throw new Error('An error occurred');
})
.then(console.log)
.catch(err => {
    console.error('Error:', err.message)
    return 10;
})
.then(console.log)
.finally(() => {
    console.log('Promise settled');
})
