function solve() {
  const outputDiv = document.getElementById('output');
  const unformatedText = document.getElementById('input');
  let cleanedText = unformatedText.value.split('.').filter(el => (el.length > 0 && el !== ' '));
  console.log(cleanedText);
  while(cleanedText.length > 0) {
    let fragment = cleanedText.splice(0, 3).join('. ');
    let newP = document.createElement('p');
    newP.textContent = `${fragment}.`;
    outputDiv.appendChild(newP);
  }
}