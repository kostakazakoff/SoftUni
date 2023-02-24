function arrayRotation(numbers, c){
    let result = [...numbers];
    let count = c % numbers.length
    for (let i = 0; i < count; i++){
        result.push(result.shift())
    }
    console.log(result.join(' '))
}

arrayRotation([51, 47, 32, 61, 21], 2)