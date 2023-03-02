function simpleCalculator(a, b, operator) {
    const calc = {
        'multiply': a * b,
        'divide': a / b,
        'add': a + b,
        'subtract': a - b
    }
    console.log(calc[operator])
}
