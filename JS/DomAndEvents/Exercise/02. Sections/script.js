function create(words) {
   const content = document.getElementById('content')
   words.forEach(word => createSection(word));

   function createSection(text) {
      let div = document.createElement('div');
      let p = document.createElement('p');
      p.textContent = text;
      p.style.display = 'none';
      div.appendChild(p);
      div.addEventListener('click', () => p.style.display = 'block');
      content.appendChild(div);
   }
}