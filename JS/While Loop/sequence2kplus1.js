function sequence(input){
    let n = input[0];
    let number = 1;
    while(number <= n){
        console.log(number);
        number = number * 2 + 1;
    }
}

// sequence(["8"])