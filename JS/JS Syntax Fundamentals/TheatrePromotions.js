function ticketPrice(day, age) {
    if (age >= 0 && age <= 18) {
        switch (day) {
            case 'Weekday':
                return console.log('12$');
            case 'Weekend':
                return console.log('15$');
            case 'Holiday':
                return console.log('5$');
        }
    } else if (age > 18 && age <= 64) {
        switch (day) {
            case 'Weekday':
                return console.log('18$');
            case 'Weekend':
                return console.log('20$');
            case 'Holiday':
                return console.log('12$');
        }
    } else if (age > 64 && age <= 122) {
        switch (day) {
            case 'Weekday':
                return console.log('12$');
            case 'Weekend':
                return console.log('15$');
            case 'Holiday':
                return console.log('10$');
        }
    } else {
        console.log('Error!')
    }
}