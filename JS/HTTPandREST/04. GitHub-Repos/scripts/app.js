function loadRepos() {
   const outputField = document.getElementById('res');
   const URL = 'https://api.github.com/users/testnakov/repos';
   fetch (URL, {method: 'GET'})
   .then (response => response.text())
   .then (data => {
      outputField.textContent = data;
   })
   .catch ((err) => {
      console.error(err);
   })
}