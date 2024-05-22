document.getElementById('add_item').addEventListener('click', () => {
    const addedItem = document.createElement('li');
    addedItem.textContent = 'Item';

    const myList = document.querySelector('.my_list');
    myList.appendChild(addedItem);
});