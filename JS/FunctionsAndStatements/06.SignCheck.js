function signCheck(...numbers) {
    let negativeNumbers = numbers.filter(n => n < 0);
    negativeNumbers.length % 2 === 0 ? console.log('Positive') : console.log('Negative');
}
