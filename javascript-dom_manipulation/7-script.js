document.addEventListener('DOMContentLoaded', function () {
  const movieListElement = document.getElementById('list_movies');

  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      const movies = data.results;

      movies.forEach(movie => {
        const titleElement = document.createElement('li');
        titleElement.textContent = movie.title;
        movieListElement.appendChild(titleElement);
      });
    })
    .catch(error => {
      console.error('Fetch error:', error);
    });
});
