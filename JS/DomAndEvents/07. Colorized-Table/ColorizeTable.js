function colorize() {
    Array.from(document.querySelectorAll('table tr:nth-child(even)'))
    .forEach(el => el.style.backgroundColor = 'Teal')
}