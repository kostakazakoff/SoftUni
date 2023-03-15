function sequences(arrOfArrays) {
    let result = new Set();
    arrOfArrays
    .map(arr => JSON.parse(arr).map(Number).sort((a, b) => b - a))
    .sort((a, b) => a.length - b.length)
    .forEach(element => {
        result.add(JSON.stringify(element));
    });
    result = Array.from(result);
    result.forEach(el => {
        el = JSON.parse(el);
        console.log(`[${el.join(', ')}]`);
    });
}

// sequences(
//     [
//         "[-3, -2, -1, 0, 1, 2, 3, 4]",
//         "[10, 1, -17, 0, 2, 13]",
//         "[4, -3, 3, -2, 2, -1, 1, 0]"
//     ]
// )