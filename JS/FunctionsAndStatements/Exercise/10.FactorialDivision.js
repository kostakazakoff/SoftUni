function factorialDivision(a, b) {
    let numbers = [a, b];
    let both = [];

    numbers.forEach(n => {
        factorial(n);
        both.push(factorial(n));
    });

    function factorial(n) {
        if (n === 0) {
            return 1;
        }
        return n * factorial(n - 1)
    }

    let output = both.reduce((n1, n2) => n1 / n2);
    console.log(output.toFixed(2))
}

// factorialDivision(6, 2)



// console.log(factorial(5))