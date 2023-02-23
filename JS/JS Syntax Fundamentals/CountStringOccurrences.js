function solve(text, word){
    let counter = 0;
    let arr = text.split(' ');
    arr.forEach(element => {
        if (element === word){
            counter += 1;
        }
    });
    console.log(counter)
}
