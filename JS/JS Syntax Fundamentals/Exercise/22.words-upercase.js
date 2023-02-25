function wordsUppercase(sentence){
    result = [];
    const regex = /[^A-z]+/g;
    let sentAsArr = sentence.split(regex)
    .forEach(word => {
        if (word){
            result.push(word.toUpperCase());
        } 
    });
    console.log(result.join(', '))
}

// wordsUppercase('Hi, how are you?')