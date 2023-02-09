function checkDayOfWeek(input){
    let output = ''
    let day = input[0]
    switch(day){
        case('Monday'):
        case('Tuesday'):
        case('Wednesday'):
        case('Thursday'):
        case('Friday'): output = 'Working day'; break;
        case('Saturday'):
        case('Sunday'): output = 'Weekend'; break;
        default: output = 'Error'; break;
    }
    console.log(output)
}

checkDayOfWeek(["Sunday"])