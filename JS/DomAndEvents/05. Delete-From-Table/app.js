function deleteByEmail() {
    const inputField = document.querySelector('input[name="email"]');
    const resultField = document.getElementById('result');
    const tds = Array.from(document.querySelectorAll("td:nth-child(2)"));
    let foundTd = tds.find(el => el.textContent === inputField.value);
    if (foundTd) {
        foundTd.parentElement.remove();
        resultField.textContent = 'Deleted.';
    } else {
        resultField.textContent = 'Not found.'
    }
}