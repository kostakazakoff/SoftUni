function parking(arr) {
    carsInParking = [];
    Object.entries(
        arr.reduce((data, car) => {
            [carStatus, number] = car.split(', ');
            data[number] = carStatus;
            return data;
        }, {})
    ).forEach(car => {
        if (car[1] == 'IN') {
            carsInParking.push(car[0]);
        }
    })

    let sorted = carsInParking.sort()
    if (sorted) {
        carsInParking.forEach(car => console.log(car));
    } else {
        console.log('Parking Lot is Empty')
    }
}


// parking(
//     [
//         'IN, CA2844AA',
//         'IN, CA1234TA',
//         'OUT, CA2844AA',
//         'IN, CA9999TT',
//         'IN, CA2866HI',
//         'OUT, CA1234TA',
//         'IN, CA2844AA',
//         'OUT, CA2866HI',
//         'IN, CA9876HH',
//         'IN, CA2822UU'
//     ]
// )