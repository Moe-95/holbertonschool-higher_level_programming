document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const selectedElement = document.getElementById('hello');
      selectedElement.textContent = data.hello;
    })
    .catch(error => {
      console.error('fetch error', error);
    });
});
