const button = document.querySelector('button');
const scrollable = document.getElementById("scrollable");
// const abortController = new AbortController();
// button.addEventListener('click', onClick, {
//     capture: true, // if true, event listener fires in capture phase instead of bubbling phase
//     once: true, // if true it removes the event once already fired
//     passive: true, // if true it will not call e.preventDefault()
//     signal: abortController.signal // removes the event listener
// });
button.addEventListener('click', onClick);
button.removeEventListener('click', onClick);

function onClick(e){
   // e.stopPropagation();
    console.log(e.target);
    console.log(this);
}