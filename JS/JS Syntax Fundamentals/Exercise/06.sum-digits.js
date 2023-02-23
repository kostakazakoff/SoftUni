function sumDigits(number){
    let numberAsArr = number.toString().split('')
    console.log(numberAsArr.reduce((a, b) => Number(a) + Number(b), 0))
}