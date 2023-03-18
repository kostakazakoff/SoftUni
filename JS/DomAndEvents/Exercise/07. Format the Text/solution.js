function solve() {
  const outputDiv = document.getElementById('output');
  const unformatedText = document.getElementById('input');
  const fragment = new DocumentFragment();
  let cleanedText = unformatedText.value.split('.').filter(el => (el.length > 0 && el !== ' '));
  while(cleanedText.length > 0) {
    let textSlice = cleanedText.splice(0, 3).join('. ');
    let newP = document.createElement('p');
    newP.textContent = `${textSlice}.`;
    fragment.appendChild(newP);
  }
  outputDiv.appendChild(fragment);
}