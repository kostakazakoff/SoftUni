function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const searchTxt = document.getElementById('searchField');
      const allFields = Array.from(document.querySelectorAll('tbody td'));
      allFields.forEach(el => el.parentElement.removeAttribute('class'));
      allFields.filter(el  => (el.textContent.toLowerCase().includes(searchTxt.value.toLowerCase()) && searchTxt.value !== ''))
      .forEach(el => el.parentElement.className = 'select');
      searchTxt.value = '';
   }
}