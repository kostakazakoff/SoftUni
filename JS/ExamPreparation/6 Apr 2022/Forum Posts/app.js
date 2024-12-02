window.addEventListener("load", solve);

function solve() {
  const form = document.querySelector('form');
  const title = document.getElementById('post-title');
  const category = document.getElementById('post-category');
  const content = document.getElementById('post-content');

  const publishBtn = document.getElementById('publish-btn');
  publishBtn.addEventListener('click', publish);

  const reviewList = document.getElementById('review-list');
  const publishedList = document.getElementById('published-list');
  const clearBtn = document.getElementById('clear-btn');
  clearBtn.addEventListener('click', clear);

  function publish() {
    const validInput = [title, category, content].every(field => field.value.length !== 0);
    if (!validInput) { console.log('invalid'); return; };

    const li = createHTMLElement('li', reviewList, null, ['rpost']);
    const article = createHTMLElement('article', li);
    createHTMLElement('h4', article, title.value);
    createHTMLElement('p', article, `Category: ${category.value}`);
    createHTMLElement('p', article, `Content: ${content.value}`);
    const editBtn = createHTMLElement('button', li, 'Edit', ['action-btn', 'edit']);
    const approveBtn = createHTMLElement('button', li, 'Approve', ['action-btn', 'approve']);
    form.reset();

    editBtn.addEventListener('click', edit);
    approveBtn.addEventListener('click', approve);
  }

  function edit() {
    console.log(this.parentNode.querySelectorAll('p')[0])
    title.value = this.parentNode.querySelector('h4').textContent;
    category.value = this.parentNode.querySelectorAll('p')[0].textContent.split(': ')[1];
    content.value = this.parentNode.querySelectorAll('p')[1].textContent.split(': ')[1];
    this.parentNode.remove();
  }

  function approve() {
    publishedList.appendChild(this.parentNode);
    publishedList.querySelector('button').remove();
    publishedList.querySelector('button').remove();
  }

  function clear() {
    this.parentNode.parentNode.querySelector('.rpost').remove();
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
