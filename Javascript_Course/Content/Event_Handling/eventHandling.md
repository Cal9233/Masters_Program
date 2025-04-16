I Event-Driven Programming
A programming paradigm where code runs as a response to events, usually initiated by the user.
To create an event listener, use element.addEventListener (eventName, callback, useCapture) . If the third argument is true, the callback will fire during the capturing phase rather than the default bubbling phase.
Additionally, addEventListener can be called with an options object as the third parameter instead of the useCapture boolean. This object can contain the following possible values:
• capture: The same as the boolean argument option; true for capturing, false for bubbling.
• once: If true, automatically removes the event listener after the event fires once.
• passive: If true, indicates to the browser that event.preventDefault() will not be called. This is useful for the browser to optimize performance, particularly with mobile scrolling events such as touchstart and touchmove to indicate to the browser that scrolling will not be cancelled.
• signal: An AbortSignal, usually coming from an AbortController. If the signal's abort() method is called the event listener will be removed.
To remove an event listener, call element. removeEventListener (eventName, callback, seCapture) or element. removeEventListener (eventName, callback, optionsobj) with the exact same parameters as were used to create the event listener.
I Event Propagation
consists of 3 phases:
The process by which an event travels through the DOM to call event listeners on nested elements. Event propagation

1. Capturing: The event travels down from the root of the document to the event target.
2. Target: The event fires on the event target.
3. Bubbling: The event travels up from the event target to the root of the document.
   At any point in the propagation process, an event listener can call event. stopPropagation () , which will stop the propagation process.
   I Event Delegation
   The process of using a single event listener on a parent element to manually delegate events to children, rather than using event listeners on each child.
   Event delegation takes advantage of event propagation. For example, after clicking on a button, that event will bubble up to the parent container.
   In the event a container has many children that all have similar event listeners, event delegation can make substantial performance improvements by lowering the total number of active event listeners. The event. target property can then be used to determine which child was the source of the event.

## Event Propogation Process

1. Capturing Phase: Event fires and starts at the root of the DOM. Honing on the target, traversing down the DOM.
2. Targeting Phase: Find the event on the element.
3. Bubbling Phase: Moves back up to the DOM.

To change the default behaviour of Event Propogation you need to call event.stopPropogation() which stops propogation process wheverever you are.
So the bubbling phase wont happen.

## Event Default

If you want to stop the default behaviour of an event you would call event.preventDefault();
