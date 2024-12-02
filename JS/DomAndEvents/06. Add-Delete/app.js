function addItem() {
    const inputText = document.getElementById('newItemText');
    const newItem = document.createElement('li');
    const newAnchor = document.createElement('a');
    newItem.textContent = inputText.value;
    newAnchor.textContent = '[Delete]';
    newAnchor.href = '#';
    newItem.appendChild(newAnchor);
    document.getElementById('items').appendChild(newItem);
    inputText.value = '';
    newAnchor.addEventListener('click', (e) => newAnchor.parentElement.remove());
}