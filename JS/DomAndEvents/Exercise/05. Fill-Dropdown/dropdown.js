function addItem() {
    const textInput = document.getElementById('newItemText');
    const valueInput = document.getElementById('newItemValue');
    let newOption = document.createElement('option');
    newOption.textContent = textInput.value;
    newOption.value = valueInput.value;
    document.getElementById('menu').appendChild(newOption);
    textInput.value = '';
    valueInput.value = '';
}