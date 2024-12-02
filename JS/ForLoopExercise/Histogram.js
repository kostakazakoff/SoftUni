function histogram(input) {
    let numbersCount = input[0];
    let numbersLen = input.length - 1;
    let output = [];
    const p = {p1Count: 0, p2Count: 0, p3Count: 0, p4Count: 0, p5Count: 0};
    for (let i = 1; i <= numbersCount; i++) {
        let number = Number(input[i]);
        if ( number < 200) {p.p1Count++}
        else if (number < 400) {p.p2Count++;}
        else if (number < 600) {p.p3Count++;}
        else if (number < 800) {p.p4Count++;}
        else {p.p5Count++;}
    }
    for (let x in p){
        output.push(`${(p[x] * 100 / numbersLen).toFixed(2)}%`)
    }
    console.log(output.join('\n'))
}

// function histogram(input) {
//     let numbersCount = input[0];
//     let numbersLen = input.length - 1;
//     let output = '';
//     const p = {p1Count: 0, p2Count: 0, p3Count: 0, p4Count: 0, p5Count: 0};
//     for (let i = 1; i <= numbersCount; i++) {
//         let number = Number(input[i]);
//         if ( number < 200) {p.p1Count++}
//         else if (number < 400) {p.p2Count++;}
//         else if (number < 600) {p.p3Count++;}
//         else if (number < 800) {p.p4Count++;}
//         else {p.p5Count++;}
//     }
//     for (let x in p){
//         output += `${(p[x] * 100 / numbersLen).toFixed(2)}%\n`
//     }
//     console.log(output.trimEnd())
// }

// histogram(["3", "1", "2", "999"])
