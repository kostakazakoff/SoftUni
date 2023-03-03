function pointsValidation(arr) {
    let distances = [
        [arr[0], arr[1], 0, 0],
        [arr[2], arr[3], 0, 0],
        [arr[0], arr[1], arr[2], arr[3]]
    ];

    const isValid = (x1, y1, x2, y2) => Number.isInteger((Math.sqrt((x2 - x1)**2 + (y2 - y1)**2)));

    distances.forEach(a => {
        isValid(a[0], a[1], a[2], a[3]) ?
            console.log(`{${a[0]}, ${a[1]}} to {${a[2]}, ${a[3]}} is valid`) :
            console.log(`{${a[0]}, ${a[1]}} to {${a[2]}, ${a[3]}} is invalid`)
    });
}

// pointsValidation([2, 1, 1, 1])