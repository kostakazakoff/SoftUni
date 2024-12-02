function numModification(number) {
    function end() {
        let numAsArr = number.toString().split('').map(Number);
        return numAsArr.reduce((a, b) => a + b) / numAsArr.length > 5;
    }
    while (!end()) {
        number += '9';
    }
    console.log(number);
}

// numModification(12)