const headerElement = document.querySelector('header');

const redHeader = document.getElementById('red_header');

// Ajouter un écouteur d'événements pour l'événement 'click'
redHeader.addEventListener('click', () => {
  headerElement.style.color = '#FF0000';
});
