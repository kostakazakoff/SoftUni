function sumTable() {
    document.getElementById('sum')
    .textContent = Array
    .from(document.querySelectorAll('table:first-child tr:not(:last-child) td:nth-child(even)'))
    .map(num => Number(num.textContent)).reduce((a, b) => a + b);
}