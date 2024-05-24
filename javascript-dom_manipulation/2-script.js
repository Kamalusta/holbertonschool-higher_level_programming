const click = document.querySelector('#red_header');
const header = document.querySelector('header');
click.addEventListener('click', () => {
  header.classList.add('red');
});
