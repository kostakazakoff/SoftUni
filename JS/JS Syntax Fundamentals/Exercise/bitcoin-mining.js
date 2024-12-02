function bitcoinBuy(daysYeld){
    let bitcoinPrice = 11949.16;
    let goldPrice = 67.51;
    let dayProfit;
    let money = 0;
    let day = 0;
    let boughtBitcoins = 0;
    let firstBitcoin = true;
    let firstBoughtBitcoinDay;
    let bitcoinsForDay;
    for (let i = 0; i < daysYeld.length; i++){
        day = i + 1;
        dayProfit = daysYeld[i] * goldPrice;
        if (day % 3 == 0){
            dayProfit -= dayProfit * 0.3;
        }
        money += dayProfit;
        if (money >= bitcoinPrice){
            bitcoinsForDay = Math.floor(money / bitcoinPrice)
            boughtBitcoins += bitcoinsForDay;
            money -= bitcoinsForDay * bitcoinPrice;
            if (firstBitcoin){
                firstBoughtBitcoinDay = day;
                firstBitcoin = false;
            };
        };
    };
    console.log(`Bought bitcoins: ${boughtBitcoins}`);
    if (firstBoughtBitcoinDay){
        console.log(`Day of the first purchased bitcoin: ${firstBoughtBitcoinDay}`);
    };
    console.log(`Left money: ${money.toFixed(2)} lv.`);
}

bitcoinBuy([3124.15, 504.212, 2511.124])