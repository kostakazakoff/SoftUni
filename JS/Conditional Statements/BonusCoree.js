function bonusScore(input){
    let points = Number(input[0]);
    let bonusPoints = 0.0;
    if (points <= 100){
        bonusPoints = 5;
    }
    else if (points <= 1000){
        bonusPoints = points * 0.2; 
    }
    else{
        bonusPoints = points * 0.1;
    }
    if (points % 2 === 0){
        bonusPoints += 1;
    }
    else if (points % 10 === 5){
        bonusPoints += 2;
    }

    console.log(bonusPoints);
    console.log(bonusPoints + points);
}

// bonusScore(["15875"])