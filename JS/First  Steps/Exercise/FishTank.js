function calcWaterCapacity(params) {
    let length = Number(params[0]) / 10;
    let width = Number(params[1]) / 10;
    let height = Number(params[2]) / 10;
    let percent = Number(params[3]) / 100;
    let totalWaterCapacity = length * width * height * (1 - percent)
    console.log(totalWaterCapacity)
}