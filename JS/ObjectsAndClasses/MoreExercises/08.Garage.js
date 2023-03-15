function garage(arr) {
    function parseStr(str) {
        return str.split(':').join(' -');
    }
    
    Object.entries(
        arr.reduce((data, str) => {
            let [garageN, carInfo] = str.split(' - ');
            if (!data[garageN]) {
                data[garageN] = [];
            }
            data[garageN].push(`--- ${parseStr(carInfo)}`);
            return data;
        }, {}))
        .forEach(([k, v]) => {
        console.log(`Garage № ${k}`);
        console.log(v.join('\n'));
    });
}

// garage(
//     [
//         '1 - color: blue, fuel type: diesel',
//         '1 - color: red, manufacture: Audi',
//         '2 - fuel type: petrol',
//         '4 - color: dark blue, fuel type: diesel, manufacture: Fiat'
//     ]
// )