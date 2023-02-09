function calcLunchBreak(input){
    let movie = input[0];
    let movieTime = Number(input[1]);
    let breakTime = Number(input[2]);
    let lunchTime = breakTime / 8;
    let restTime = breakTime / 4;
    let timeLeft = breakTime - lunchTime - restTime;
    let difference = Math.ceil(Math.abs(timeLeft - movieTime));
    if (timeLeft >= movieTime){
        console.log(`You have enough time to watch ${movie} and left with ${difference} minutes free time.`);
    }
    else{
        console.log(`You don't have enough time to watch ${movie}, you need ${difference} more minutes.`);
    }
}

// calcLunchBreak(["Game of Thrones", "60", "96"])