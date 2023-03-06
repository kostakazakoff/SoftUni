function printDna(n) {
    let symbols;
    let line;
    const dnaSeq = 'ATCGTTAGGG'.match(/[A-Z]{2}/g);

    for (let i = 0; i < n; i++) {
        let stars = '';
        let dashes = '';
        symbols = dnaSeq[i % dnaSeq.length].split('');

        if (i % 4 === 0) {
            stars = '*'.repeat(2);
        } else if (i % 2 !== 0) {
            stars = '*';
            dashes = '-'.repeat(2);
        } else if (i % 2 === 0 && i % 2 !== 4) {
            dashes = '-'.repeat(4);
        }

        line = `${stars}${symbols[0]}${dashes}${symbols[1]}${stars}`;
        console.log(line);
    }
}

// printDna(10)