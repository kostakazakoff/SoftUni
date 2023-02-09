function EvenOdd(params) {
    let number = Number(params[0]);
    let even = number % 2 == 0;
    if (even) {console.log("even")}
    else {console.log("odd")}
}