function calcCircleArea(input){
    let inputType = typeof(input);
    if (inputType === 'number'){
        let area = Math.pow(input, 2) * Math.PI;
        console.log(area.toFixed(2));
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${inputType}.`);
    }
}
