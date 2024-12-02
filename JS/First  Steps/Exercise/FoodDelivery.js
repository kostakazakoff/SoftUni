function calcOrder(params) {
    let chicken = Number(params[0]) * 10.35;
    let fish = Number(params[1]) * 12.4;
    let vegetarean = Number(params[2]) * 8.15;
    let mainDish = chicken + fish + vegetarean
    let dessert = mainDish * 0.2
    let delivery = 2.5
    let totalPrice = mainDish + dessert + delivery
    console.log(totalPrice)
}