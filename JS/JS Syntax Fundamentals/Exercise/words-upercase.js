function wordsUppercase(sentence){
    result = [];
    const regex = /[^\w]+/g;
    let sentAsArr = sentence.split(regex)
    .forEach(word => {
        if (word){
            result.push(word.toUpperCase());
        } 
    });
    console.log(result.join(', '))
}

// wordsUppercase('Hi, how are you?')