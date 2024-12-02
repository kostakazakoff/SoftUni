function meetings(arr) {
    let meetingsObj = {};
    arr.forEach(meet => {
        [day, person] = meet.split(' ');

        if (!meetingsObj.hasOwnProperty(day)) {
            meetingsObj[day] = person;
        console.log(`Scheduled for ${day}`);
        } else {
            console.log(`Conflict on ${day}!`);
        }

    });

    for (day in meetingsObj) {
        console.log(`${day} -> ${meetingsObj[day]}`);
    }
}

// meetings(['Monday Peter',
// 'Wednesday Bill',
// 'Monday Tim',
// 'Friday Tim']
// )