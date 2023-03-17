function subtract() {
    document.getElementById('result')
    .textContent = Array
    .from(document.querySelectorAll('input'))
    .map(el => Number(el.value)).reduce((n1, n2) => n1 - n2)
}