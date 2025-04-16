const listItems = document.querySelectorAll("li");

// adding style
listItems[0].setAttribute("class", "big blue");
listItems[0].classList.add("blue");

//creating own DOM node
const p = document.createElement("p");
// can use createTextNode or innerHTML to create text and append
const text = document.createTextNode("hELLO wORLD");
p.append(text);

document.body.prepend(p);
// never use innerHTML if using user input
// document.body.innerHTML = '';

const parent = document.querySelector('ol');
const fragment = document.createDocumentFragment();
//const listItemsToAdd = [];
for(let i = 0; i < 3; i++){
    const li = document.createElement('li');
    li.textContent = `List item with i=${i}`;
    fragment.append(li);
    //listItemsToAdd.push(li);
}
//parent.append(...listItemsToAdd);
parent.append(fragment);

//listItems[0].parentNode.removeChild(listItems[0])
listItems[0].remove();