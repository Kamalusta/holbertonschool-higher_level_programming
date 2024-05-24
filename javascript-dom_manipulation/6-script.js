const nameChar = document.querySelector('#character');
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((response) => response.json())
  .then((data) => {
    nameChar.innerHTML = data.name;
  })
  .catch(() => {
    nameChar.innerHTML = 'Error loading character';
  });
