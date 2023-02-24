function stringSubstring(word, sequence){
    let found = false;
    sequence.split(' ')
    .forEach(element => {
        if (word.toLowerCase() === element.toLowerCase()){
            console.log(word);
            found = true;
            return;
        }
    });
    if (!found){
        console.log(`${word} not found!`)
    }
}

// stringSubstring('javascript',
// 'JavaScript is the best programming language'
// )