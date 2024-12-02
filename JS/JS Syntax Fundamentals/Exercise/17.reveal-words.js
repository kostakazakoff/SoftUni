function revealWords(w, s){
    const regex = /\*+/g;
    let words = w.split(', ');
    let sequence = s.split(' ');
    for (let idx = 0; idx < sequence.length; idx++){
        let point = sequence[idx].match(regex);
        if (point){
            for (const word of words){
                if (word.length === sequence[idx].length){
                    sequence[idx] = word;
                }
            }
        }
    }
    console.log(sequence.join(' '))
}

// revealWords('great, learning',
// 'softuni is ***** place for ******** new programming languages'
// )