function fruitPrice(fruit, grams, priceForKg){
    let kg = grams / 1000;
    let price = priceForKg * kg;
    console.log(`I need $${price.toFixed(2)} to buy ${kg.toFixed(2)} kilograms ${fruit}.`)
}