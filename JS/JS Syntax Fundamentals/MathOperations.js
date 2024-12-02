function operation(a, b, operator) {
    switch (operator) {
        case '+':
            return console.log(a + b);
        case '-':
            return console.log(a - b);
        case '*':
            return console.log(a * b);
        case '/':
            return console.log(a / b);
        case '%':
            return console.log(a % b);
        case '**':
            return console.log(a ** b);
    }
}
