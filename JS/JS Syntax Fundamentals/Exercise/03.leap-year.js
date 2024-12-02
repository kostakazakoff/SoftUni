function leapYear(year){
    leap = year % 4  === 0 && year % 100 !== 0 || year % 400 === 0;
    if (leap){
        console.log('yes');
    } else {
        console.log('no')
    }
}