function calcExpenses(input) {
    let budget = Number(input[0]);
    let people = Number(input[1]);
    let wear = Number(input[2]) * people;
    let decor = budget * 0.1;
    if (people > 150) {
        wear = wear - wear * 0.1;
    }
    let totalExpenses = decor + wear;
    let difference = Math.abs(budget - totalExpenses);
    if (totalExpenses > budget){
        console.log("Not enough money!");
        console.log(`Wingard needs ${difference.toFixed(2)} leva more.`);
    }
    else{
        console.log("Action!");
        console.log(`Wingard starts filming with ${difference.toFixed(2)} leva left.`);
    }
}

// calcExpenses(["9587.88", "222", "55.68"])