function search() {
   const towns = Array.from(document.querySelectorAll('li'));
   const searchField = document.querySelector('#searchText')
   const output = document.querySelector('#result');
   let count = 0;

   towns.forEach(t => {
      if (t.textContent.toLowerCase().includes(searchField.value.toLowerCase()) && searchField.value.length !== 0) {
         t.style.textDecoration = 'underline';
         t.style.fontWeight = 'bold';
         count++;
      } else {
         t.style.textDecoration = 'none';
         t.style.fontWeight = 'normal';
      }
   });
   output.textContent = `${count} matches found`
   searchField.value = '';
   count = 0;
}
