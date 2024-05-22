// Select the element with the id 'red_header' and assign it to the variable 'selectedElement'
const selectedElement = document.querySelector('#red_header');

// Add an event listener for the 'click' event to the 'selectedElement'
selectedElement.addEventListener('click', () => {
  // When 'selectedElement' is clicked, this anonymous function is executed.

  // Add the 'red' class to 'selectedElement'
  selectedElement.classList.add('red');
});
