const list = document.querySelector('#list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    data.results.forEach(element => {
      const li = document.createElement('li');
      li.innerText = element.title;
      list.appendChild(li);
    });
  });
