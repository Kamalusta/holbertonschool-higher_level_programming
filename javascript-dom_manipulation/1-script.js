const click = document.querySelector('#red_header');
const header = document.querySelector('header');
click.addEventListener('click', (e) => {
  header.style.color = '#FF0000';
});
