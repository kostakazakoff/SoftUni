function FlightSchedule(matrix) {
    let [flightsArr, changesArr, statusToCheck] = matrix;
    const changedFlightStatuses = statusToCheck == 'Cancelled';

    function parseToObj(arr) {
        let obj = arr.reduce((data, flght, info) => {
            [flght, ...info] = flght.split(' ');
            info = info.join(' ');
            data[flght] = [`Destination: '${info}'`, `Status: 'Ready to fly'`];
            return data;
        }, {})
        return obj;
    }

    let flights = parseToObj(flightsArr);

    for (let info of changesArr) {
        info = info.split(' ');
        let flightNumber = info[0];
        let statusChange = info[1];
        flightToChange = flights[flightNumber];
        if (flightToChange) {
            flights[flightNumber][1] = `Status: '${statusChange}'`;
        }
    }

    function print(status) {
        for (let number in flights) {
            if (flights[number][1] == status) {
                console.log(`{ ${flights[number].join(', ')} }`);
            }
        }
    }

    if (changedFlightStatuses) {
        print("Status: 'Cancelled'");
    } else {
        print("Status: 'Ready to fly'");
    }
}


// FlightSchedule([['WN269 Delaware',
// 'FL2269 Oregon',
//  'WN498 Las Vegas',
//  'WN3145 Ohio',
//  'WN612 Alabama',
//  'WN4010 New York',
//  'WN1173 California',
//  'DL2120 Texas',
//  'KL5744 Illinois',
//  'WN678 Pennsylvania'],
//  ['DL2120 Cancelled',
//  'WN612 Cancelled',
//  'WN1173 Cancelled',
//  'SK330 Cancelled'],
//  ['Ready to fly']
// ]
// )