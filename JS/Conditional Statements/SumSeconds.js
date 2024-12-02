function sumSeconds(input){
    let first = parseInt(input[0]);
    let second = parseInt(input[1]);
    let third = parseInt(input[2]);
    let totalSeconds = first + second + third;
    let minutes = Math.floor(totalSeconds / 60);
    let seconds = totalSeconds % 60;

    if (seconds < 10){
        seconds = `0${seconds}`;
    }
    console.log(`${minutes}:${seconds}`);
};

// sumSeconds(["35", "45", "44"])
