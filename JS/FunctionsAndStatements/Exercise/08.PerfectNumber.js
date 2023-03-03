function perfectNumber(number) {
    let dividers = [];
    const isDivider = (divider) => number % divider === 0;
    const isPerfect = (arrOfDividers) => arrOfDividers.reduce((a, b) => a + b) === number;
    for (let divider = 1; divider < number; divider++) {
        if (isDivider(divider)) {
            dividers.push(divider);
        }
    }
    isPerfect(dividers) ? console.log('We have a perfect number!') : console.log("It's not so perfect.");
}

// perfectNumber(1236498)