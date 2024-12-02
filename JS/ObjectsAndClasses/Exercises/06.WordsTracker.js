function wordsTracker([searchWords, ...sentence]) {
    searchWords = searchWords.split(' ')
    Object.entries(
        searchWords.reduce((data, word) => {
            let count = sentence.filter(el => el == word).length;
            data[word] = count;
            return data;
        }, {})
    )
    .sort((a, b) => b[1] - a[1])
    .forEach(line => console.log(`${line[0]} - ${line[1]}`))
}

// wordsTracker([
//     'sentence this',
//     'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
// ]
// )