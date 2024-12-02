window.addEventListener("load", solve);

function solve() {
  const form = document.querySelector('form');
  const inputDOMSelectors = {
    firstName: document.getElementById('first-name'),
    lastName: document.getElementById('last-name'),
    age: document.getElementById('age'),
    gender: document.getElementById('genderSelect'),
    description: document.getElementById('task')
  }
  const submitBtn = document.getElementById('form-btn');
  const clearBtn = document.getElementById('clear-btn');

  const inProgress = document.getElementById('in-progress');
  const progressCounter = document.getElementById('progress-count');
  const finished = document.getElementById('finished');

  let casch = {};
  let counter = 0;

  submitBtn.addEventListener('click', toInProgtress);
  clearBtn.addEventListener('click', clear);

  function toInProgtress() {
    const inputIsValid = Object.values(inputDOMSelectors).every(field => field.value.length > 0);
    if (!inputIsValid) { return; }

    inProgress.innerHTML = '<h3>In progress</h3>';

    const { firstName, lastName, age, gender, description } = inputDOMSelectors;
    casch = {
      firstName: firstName.value,
      lastName: lastName.value,
      age: age.value,
      gender: gender.value,
      description: description.value
    }

    const li = createHTMLElement('li', inProgress, null, ['each-line']);
    const article = createHTMLElement('article', li);
    createHTMLElement('h4', article, `${casch.firstName} ${casch.lastName}`);
    createHTMLElement('p', article, `${casch.gender}, ${casch.age}`);
    createHTMLElement('p', article, `Dish description: ${casch.description}`);

    const editBtn = createHTMLElement('button', li, 'Edit', ['edit-btn']);
    const completeBtn = createHTMLElement('button', li, 'Mark as complete', ['complete-btn']);

    form.reset();

    editBtn.addEventListener('click', edit);
    completeBtn.addEventListener('click', complete);

    counter++;
    progressCounter.textContent = counter;
  }

  function edit() {
    for (const key in casch) {
      inputDOMSelectors[key].value = casch[key];
    }
    counter--;
    progressCounter.textContent = counter;
    this.parentNode.remove();
  }

  function complete() {
    finished.appendChild(this.parentNode);
    finished.querySelector('button').remove();
    finished.querySelector('button').remove();

    counter--;
    progressCounter.textContent = counter;
  }

  function clear() {
    finished.innerHTML = '';
  }

  function createHTMLElement(type, parentNode, content, classes, id, attributes, useInnerHtml) {
    const htmlElement = document.createElement(type);

    if (content && useInnerHtml) {
      htmlElement.innerHTML = content;
    } else {
      if (content && type !== 'input') {
        htmlElement.textContent = content;
      }

      if (content && type === 'input') {
        htmlElement.value = content;
      }
    }

    if (classes && classes.length > 0) {
      htmlElement.classList.add(...classes);
    }

    if (id) {
      htmlElement.id = id;
    }

    // { src: 'link', href: 'http' }
    if (attributes) {
      for (const key in attributes) {
        htmlElement.setAttribute(key, attributes[key])
      }
    }

    if (parentNode) {
      parentNode.appendChild(htmlElement);
    }

    return htmlElement;
  }
}
