function extractText() {
    let output = [];
    Array.from(document.querySelectorAll('#items li'))
    .forEach(item => output.push(item.textContent))
    document.getElementById('result').value = output.join('\n');
}