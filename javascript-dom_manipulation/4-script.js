const add = document.querySelector('#add_item');
const list = document.querySelector('.my_list');
add.addEventListener('click', () => {
  const li = document.createElement('li');
  list.appendChild(li);
  li.after('Item');
});
