document.addEventListener('DOMContentLoaded', function () {
  const selectedElement = document.getElementById('character');

  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      const characterName = data.name;

      selectedElement.textContent = `Character: ${characterName}`;
    })
    .catch(error => {
      console.error('Fetch error:', error);
    });
});
