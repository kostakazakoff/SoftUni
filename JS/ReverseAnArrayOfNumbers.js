function reverseArray(n, list){
    let arr = [];
    let arrToReverse = list.slice(0, n)
    arrToReverse.forEach(element => {
        arr.unshift(element);
    });
    let output = arr.join(' ')
    console.log(output)
}
