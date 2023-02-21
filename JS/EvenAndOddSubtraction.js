function solve(arr){
    let evens = 0;
    let odds = 0;
    arr.forEach(element => {
        if (element % 2 === 0){
            evens += element;
        } else {
            odds += element;
        }
    });
    console.log(evens - odds)
}
