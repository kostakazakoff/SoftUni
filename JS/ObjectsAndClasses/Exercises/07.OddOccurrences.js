function oddOccurrencesCount(str) {
    let output = [];
    let arr = str.split(' ').map(el => el.toLowerCase());
    let uniqueElements = Array.from(new Set(arr));

    uniqueElements.forEach(el => {
        if (arr.filter(x => x == el.toLowerCase()).length % 2 !== 0) {
            output.push(el);
        }
    })
    console.log(output.join(' '));
}

// oddOccurrencesCount('Java C# Php PHP Java PhP 3 C# 3 1 5 C#')