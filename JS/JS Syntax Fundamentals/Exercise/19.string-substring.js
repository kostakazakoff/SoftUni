function stringSubstring(word, sequence){
    let found = false;
    let arr = sequence.split(' ')
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