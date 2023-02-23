function modernTimes(sentence){
    const regex = /(?<=#)[A-z]+/g;
    let result = sentence.matchAll(regex)
    for (const element of result) {
        console.log(element[0])
    }
}

// modernTimes('Nowadays everyone uses # to tag a #special word in #socialMedia')
// modernTimes('The symbol # is known #variously in English-speaking #regions as the #number sign')