function sortingNumbers(arr) {
    let result = [];
    arr.sort((a, b) => a - b);
    while(arr.length > 1){
        result.push(arr.shift());
        result.push(arr.pop());
    }
    result.push(...arr);
    return result;
}

// console.log(sortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56])) 