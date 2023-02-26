function expectedYeld(startYeld){
    let days = 0;
    let totalYeld = 0;
    while (startYeld >= 100){
        days += 1;
        totalYeld += startYeld - 26;
        startYeld -= 10;
    };
    totalYeld -= 26;
    if (totalYeld < 0){
        totalYeld = 0;
    };
    console.log(days);
    console.log(totalYeld);
}

// expectedYeld(100)