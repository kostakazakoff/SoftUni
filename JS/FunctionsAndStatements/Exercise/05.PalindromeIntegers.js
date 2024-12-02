function findPalindromeIntegers(arr) {
    const isPalindrome = (array) => array.join('') === array.reverse().join('');
    arr.forEach(integer => {
        let numberAsArray = integer.toString().split('');
        console.log(isPalindrome(numberAsArray));
    });
}

findPalindromeIntegers([123,323,421,121])

