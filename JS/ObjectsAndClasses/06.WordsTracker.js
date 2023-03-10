function wordsTracker([searchWords, ...sentence]) {
    searchWords = searchWords.split(' ')
    searchWords.reduce((data, word) => {
        let count = sentence.filter(el => el == word).length;
        data.push({ word, count });
        return data;
    }, [])
        .sort((a, b) => Object.values(b)[1] - Object.values(a)[1])
        .forEach(line => console.log(`${line.word} - ${line.count}`))
}

// wordsTracker([
//     'sentence this',
//     'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
// ]
// )