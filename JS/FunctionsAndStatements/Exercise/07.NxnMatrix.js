function printMatrix(size) {
    let matrix = Array(size).fill( Array(size).fill(size).join(' ') ).join('\n');
    console.log(matrix);
}

// printMatrix(7)