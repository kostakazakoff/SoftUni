function addItem() {
    const inputText = document.getElementById('newItemText').value;
    let newItem = document.createElement('li');
    newItem.textContent = inputText;
    document.getElementById('items').appendChild(newItem);
}