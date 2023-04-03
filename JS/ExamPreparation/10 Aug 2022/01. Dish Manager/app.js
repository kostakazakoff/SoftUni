window.addEventListener("load", solve);

function solve() {
  const inputDOMSelectors = {
    firstName: document.getElementById('first-name'),
    lastName: document.getElementById('last-name'),
    age: document.getElementById('age'),
    gender: document.getElementById('genderSelect'),
    dishDescription: document.querySelector('textarea')
  }
  const submitBtn = document.getElementById('form-btn');

  const inProgress = document.getElementById('in-progress');
  const progressCounter = document.getElementById('progress-count');

  submitBtn.addEventListener('click', toInProgtress);

  function toInProgtress() {
    
  }
}
