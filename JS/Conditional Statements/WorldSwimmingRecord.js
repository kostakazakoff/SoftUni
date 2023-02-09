function calcSwimmingTime(input){
    let record = Number(input[0]);
    let distance = Number(input[1]);
    let secFor1m = Number(input[2]);
    let sections15m = Math.floor(distance / 15);
    let time = distance * secFor1m + sections15m * 12.5;
    if (time < record){
        console.log(`Yes, he succeeded! The new world record is ${time.toFixed(2)} seconds.`)
    }
    else{
        console.log(`No, he failed! He was ${(time - record).toFixed(2)} seconds slower.`)
    }
}

// calcSwimmingTime(["55555.67", "3017", "5.03"])