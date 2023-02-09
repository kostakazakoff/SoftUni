function sumNumbers(input){
    let targetNumber = Number(input[0]);
    let idx = 1;
    let sumOfNumbers = 0;
    while(true){
        let number = Number(input[idx]);
        sumOfNumbers = number + sumOfNumbers;
        if(sumOfNumbers >= targetNumber){
            console.log(sumOfNumbers);
            break;
        }
        idx++;
    }
}

// sumNumbers(["20",
// "1",
// "2",
// "3",
// "4",
// "5",
// "6"])

