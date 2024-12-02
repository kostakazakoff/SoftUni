function printDna(n) {
    let firstChar;
    let secondChar;
    let line;
    let index;
    const dnaSeq = 'ATCGTTAGGG';

    for (let i = 0; i < n; i++) {
        let stars = '';
        let dashes = '';
        index = (i * 2 % dnaSeq.length);
        [firstChar, secondChar] = dnaSeq.slice(index, index+2).split('');

        if (i % 4 === 0) {
            stars = '*'.repeat(2);
        } else if (i % 2 !== 0) {
            stars = '*';
            dashes = '-'.repeat(2);
        } else if (i % 2 === 0 && i % 2 !== 4) {
            dashes = '-'.repeat(4);
        }

        line = `${stars}${firstChar}${dashes}${secondChar}${stars}`;
        console.log(line);
    }
}

// function printDna(n) {
//     let symbols;
//     let line;
//     const dnaSeq = 'ATCGTTAGGG'.match(/[A-Z]{2}/g);

//     for (let i = 0; i < n; i++) {
//         let stars = '';
//         let dashes = '';
//         symbols = dnaSeq[i % dnaSeq.length].split('');

//         if (i % 4 === 0) {
//             stars = '*'.repeat(2);
//         } else if (i % 2 !== 0) {
//             stars = '*';
//             dashes = '-'.repeat(2);
//         } else if (i % 2 === 0 && i % 2 !== 4) {
//             dashes = '-'.repeat(4);
//         }

//         line = `${stars}${symbols[0]}${dashes}${symbols[1]}${stars}`;
//         console.log(line);
//     }
// }

printDna(6)