function CalcFoodPrice(input) {
    let dogFoodPrice = 2.5;
    let catFoodPrice = 4;
    let dogFoodPacks = Number(input[0]);
    let catFoodPacks = Number(input[1]);
    let total = dogFoodPacks * dogFoodPrice + catFoodPacks * catFoodPrice;
    console.log(`${total} lv.`);
}