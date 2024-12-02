function calcOddAndEvenSum(number) {
    let oddNumbers = [];
    let evenNumbers = [];
    function sum(arr) {
        return arr.reduce((a, b) => a + b, 0);
    }
    number.toString().split('').map(Number).forEach(n => {
        n % 2 === 0 ? evenNumbers.push(n) : oddNumbers.push(n);
    });
    console.log(`Odd sum = ${sum(oddNumbers)}, Even sum = ${sum(evenNumbers)}`);
}

calcOddAndEvenSum(3495892137259234)