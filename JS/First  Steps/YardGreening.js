function calcExpenses(param) {
    let sqM = Number(param);
    let pricePerSqm = 7.61;
    let price = sqM * pricePerSqm;
    let discount = price * 0.18;
    let total =  price - discount;
    console.log(`The final price is: ${total} lv.\nThe discount is: ${discount} lv.`)
}