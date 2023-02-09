function readTimeCalc(params) {
    let pages = Number(params[0]);
    let readSpeed = Number(params[1]);
    let days = Number(params[2]);
    let hoursPerBook = pages / readSpeed;
    let hoursPerDay = hoursPerBook / days;
    console.log(hoursPerDay);
}