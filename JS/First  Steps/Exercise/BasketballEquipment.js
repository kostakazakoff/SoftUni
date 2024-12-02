function calcExpences(params) {
    let fee = Number(params);
    let shoes = fee * 0.6;
    let outfit = shoes * 0.8;
    let ball = outfit * 0.25;
    let accessories = ball * 0.2;
    let totalExpences = fee + shoes + outfit + ball + accessories
    console.log(totalExpences)
}