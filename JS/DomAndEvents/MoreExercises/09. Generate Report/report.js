function generateReport() {
    const outputField = document.getElementById('output');
    const checkboxes = Array.from(document.querySelectorAll('input[type="checkbox"]'))
    const rows = document.querySelectorAll('tbody > tr').length;
    let arrOfRows = [];
    let checked = [];
    let output = [];

    for (let i in checkboxes) {
        if (checkboxes[i].checked) {
            checked.push([checkboxes[i], Number(i) + 1]);
        }
    }

    let cols = checked.length;

    for (let c = 0; c < cols; c++) {
        let colObj = [];
        for (let r = 0; r < rows; r++) {
            let name = checked[c][0].parentElement.innerText.toLowerCase().trim();
            let col = checked[c][1];
            let value = document.querySelector(`tbody tr:nth-child(${r+1}) td:nth-child(${col})`).textContent
            colObj.push({[name]: value});
        }
        arrOfRows.push(colObj);
    }

    cols = arrOfRows.length;
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            output.push(arrOfRows[c][r]);
        }
    }
    console.log(output);
    outputField.value = JSON.stringify(output)
}
