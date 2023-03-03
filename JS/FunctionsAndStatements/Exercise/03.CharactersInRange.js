function charsInRange(first, last) {
    let firstCharASCII = first.charCodeAt(0);
    let lastCharASCII = last.charCodeAt(0);

    if (firstCharASCII > lastCharASCII) {
        [firstCharASCII, lastCharASCII] = [lastCharASCII, firstCharASCII];
    }

    let charsBetween = [];
    for (let ascii = firstCharASCII + 1; ascii < lastCharASCII; ascii ++) {
        charsBetween.push(String.fromCharCode(ascii))
    }
    
    console.log(charsBetween.join(' '))
}


charsInRange('C',
'#'
)