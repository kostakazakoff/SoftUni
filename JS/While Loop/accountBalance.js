function accountBalance(input){
    let idx = 0;
    let income = input[idx];
    let balance = 0
    while(income != 'NoMoreMoney'){
        if(Number(income) < 0){
            console.log('Invalid operation!')
            break;
        }
        balance = balance + Number(income);
        console.log(`Increase: ${Number(income).toFixed(2)}`);
        idx++;
        income = input[idx];
    }
    console.log(`Total: ${balance.toFixed(2)}`)
}

// accountBalance(["120",
// "45.55",
// "-150"])

