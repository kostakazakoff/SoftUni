function sameNumbers(number){
    let same = true;
    let sum = 0;
    let numberAsArr = number.toString().split('');
    for (let i = 1; i < numberAsArr.length; i++){
        if (numberAsArr[i] !== numberAsArr [i-1]){
            same = false;
            break;
        }
    }
    sum = numberAsArr.reduce((a, b) => Number(a) + Number(b), 0)
    console.log(same)
    console.log(sum)
}

sameNumbers(1234)