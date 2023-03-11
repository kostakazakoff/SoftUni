function FlightSchedule(matrix) {
    let [flightsArr, changesArr, statusToCheck] = matrix;
    const changedFlightStatuses = statusToCheck == 'Cancelled';

    function parseToObj(arr) {
        let obj = arr.reduce((data, flght, info) => {
            [flght, ...info] = flght.split(' ');
            info = info.join(' ');
            data[flght] = [info, 'Ready to fly'];
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
            flights[flightNumber][1] = statusChange;
            let flightDestination = flights[flightNumber][0];
            changedFlightStatuses[flightDestination] = statusChange;
        }
    }

    if (changedFlightStatuses) {
        Object.entries(flights).forEach(flght => {
            if (flght[1][1] == 'Cancelled') {
                console.log(`{ Destination: '${flght[1][0]}', Status: '${flght[1][1]}' }`);
            }
        })
    } else {
        Object.entries(flights).forEach(flght => {
            if (flght[1][1] == 'Ready to fly')
                console.log(`{ Destination: '${flght[1][0]}', Status: '${flght[1][1]}' }`);
        })
    }
}


FlightSchedule([['WN269 Delaware',
'FL2269 Oregon',
 'WN498 Las Vegas',
 'WN3145 Ohio',
 'WN612 Alabama',
 'WN4010 New York',
 'WN1173 California',
 'DL2120 Texas',
 'KL5744 Illinois',
 'WN678 Pennsylvania'],
 ['DL2120 Cancelled',
 'WN612 Cancelled',
 'WN1173 Cancelled',
 'SK330 Cancelled'],
 ['Ready to fly']
]
)