function calculator(n1, operator, n2) {
    let result;
    switch (operator) {
        case '+':
            result = n1 + n2;
            break;
        case '-':
            result = n1 - n2;
            break;
        case '*':
            result = n1 * n2;
            break;
        case '/':
            result = n1 / n2;
    };
    console.log(result.toFixed(2))
}