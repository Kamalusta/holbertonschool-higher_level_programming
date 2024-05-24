document.addEventListener('DOMContentLoaded', () => {
  const hello = document.querySelector('#hello');
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => response.json())
    .then((data) => hello.innerHTML = data.hello);
});
