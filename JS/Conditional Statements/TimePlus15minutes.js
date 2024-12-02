function timePlus15min(input){
    let m = Number(input[0]) * 60 + Number(input[1]);
    let h = 0;
    m += 15;
    h = Math.floor(m / 60);
    m = m % 60;
    if (h >= 24){
        h = 0;
    }
    if (m < 10){
        m = (`0${m}`);
    }
    console.log(`${h}:${m}`);
}


timePlus15min(["23", "59"])