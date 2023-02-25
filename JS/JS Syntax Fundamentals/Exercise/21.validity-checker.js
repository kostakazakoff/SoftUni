function validityChecker(x1, y1, x2, y2){
    let vars = [
        [x1, y1, 0, 0],
        [x2, y2, 0, 0],
        [x1, x2, y1, y2],
    ]
    .forEach(arr => {
        let distX = arr[2] - arr[0];
        let distY = arr[3] - arr[1];

        let valid = Number.isInteger(Math.sqrt(distX**2 + distY**2));

        switch (valid){
            case true:
                console.log(`{${arr[0]}, ${arr[1]}} to {${arr[2]}, ${arr[3]}} is valid`);
                break;
            case false:
                console.log(`{${arr[0]}, ${arr[1]}} to {${arr[2]}, ${arr[3]}} is invalid`);
        };
    });
}

// validityChecker(3, 0, 0, 4);
// console.log('----------------------')
// validityChecker(2, 1, 1, 1);
