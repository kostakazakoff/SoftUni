function pascalSplitter(string){
    let output = []
    const regex = /[A-Z]{1}[a-z]*/g;
    let result = string.matchAll(regex);
    for (const word of result){
        output.push(word);
    }
    console.log(output.join(', '))
}

// pascalSplitter('ThisIsSoAnnoyingToDo')