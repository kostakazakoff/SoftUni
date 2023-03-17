function addItem() {
    const inputText = document.getElementById('newItemText');
    const newItem = document.createElement('li');
    newItem.textContent = inputText.value;
    document.getElementById('items').appendChild(newItem);
    inputText.value = '';
}