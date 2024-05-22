// Select the 'header' element
const selectedHeader = document.querySelector('toggle_header');

// Add an event listener for the 'click' event to the 'toggle_header' element
selectedHeader.addEventListener('click', function () {
  // Toggle the presence of the 'red' and 'green' classes on the 'selectedHeader' element
  selectedHeader.classList.toggle('red');
  selectedHeader.classList.toggle('green');
});
