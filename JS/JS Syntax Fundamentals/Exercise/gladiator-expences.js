function gladiatorExpences(lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice){
    let battlesCount;
    let expences = 0;
    for (let i = 0; i < lostFights; i++){
        battlesCount = i + 1;
        if (battlesCount % 2 === 0){
            expences += helmetPrice;
        };
        if (battlesCount % 3 === 0){
            expences += swordPrice;
        };
        if (battlesCount % 6 === 0){
            expences += shieldPrice;
        };
        if (battlesCount % 12 === 0){
            expences += armorPrice;
        };
    }
    console.log(`Gladiator expenses: ${expences.toFixed(2)} aureus`);
}

// gladiatorExpences(23,
//     12.50,
//     21.50,
//     40,
//     200
//     )