function censore(sentence, word){
    let arr = sentence.split(' ');
    while (sentence.includes(word)){
        sentence = sentence.replace(word, '*'.repeat(word.length));
    }
    console.log(sentence)
}
