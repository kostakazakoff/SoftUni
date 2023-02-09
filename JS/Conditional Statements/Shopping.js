function calcMaterials(input){
    let budget = Number(input[0]);
    let numberOVideoCards = Number(input[1]);
    let numberOfProcessors = Number(input[2]);
    let numberOfRAM = Number(input[3]);
    let videoCards = 250 * numberOVideoCards;
    let processors = videoCards * 0.35 * numberOfProcessors;
    let ram = videoCards * 0.1 * numberOfRAM;
    let total = videoCards + processors + ram;
    if (numberOVideoCards > numberOfProcessors){
        total = total - total * 0.15;
    }
    let difference = Math.abs(budget - total);
    if (total > budget){
        console.log(`Not enough money! You need ${difference.toFixed(2)} leva more!`);
    }
    else{
        console.log(`You have ${difference.toFixed(2)} leva left!`);
    }
}

// calcMaterials(["920.45", "3", "1", "1"])