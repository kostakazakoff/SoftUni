function sameNumbers(number) {
    let same = [];
    let numberAsArr = number.toString().split('');
    let sum = Number(numberAsArr[0]);
    for (let i = 1; i < numberAsArr.length; i++) {
        same.push(numberAsArr[i] === numberAsArr[i - 1]);
        sum += Number(numberAsArr[i])
    }
    console.log(same.every((n) => n))
    console.log(sum)
}