function extract(content) {
    const elContent = document.getElementById(content).innerText;
    let extracted = elContent.match(/(?<=\()[^\)]+(?=\))/g);
    return extracted.join('; ');
}