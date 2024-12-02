function attachEvents() {
  const loadBtn = document.getElementById('loadBooks');
  const form = document.getElementById('form')
  const formTitle = form.querySelector('h3');
  const [inputBookTitle, inputBookAuthor] = document.querySelectorAll('#form input');
  const submitBtn = document.querySelector('#form button');
  const booksTable = document.querySelector('tbody');
  const BASE_URL = 'http://localhost:3030/jsonstore/collections/books/';
  let editBookId;

  loadBtn.addEventListener('click', loadBooks);
  submitBtn.addEventListener('click', submit);

  function loadBooks() {
    fetch(BASE_URL)
      .then(response => response.json())
      .then((data) => outputData(data))
      .catch((error) => console.error(error));
  }

  function outputData(data) {
    booksTable.textContent = ''
    inputBookTitle.value = '';
    inputBookAuthor.value = '';
    formTitle.textContent = 'FORM'
    Object.entries(data).forEach(([bookId, book]) => {
      const tr = document.createElement('tr');
      const tdBook = document.createElement('td');
      const tdAuthor = document.createElement('td');
      const tdButtons = document.createElement('td');
      const editBtn = document.createElement('button');
      const deleteBtn = document.createElement('button');

      tdBook.textContent = book.title;
      tdAuthor.textContent = book.author;
      editBtn.textContent = 'Edit';
      editBtn.id = bookId;
      deleteBtn.textContent = 'Delete';
      deleteBtn.id = bookId;

      tdButtons.appendChild(editBtn);
      tdButtons.appendChild(deleteBtn);

      [tdBook, tdAuthor, tdButtons].forEach(el => tr.appendChild(el));
      booksTable.appendChild(tr);

      editBtn.addEventListener('click', () => {
        formTitle.textContent = 'Edit FORM';
        inputBookTitle.value = book.title;
        inputBookAuthor.value = book.author;
        editBookId = bookId;
      });

      deleteBtn.addEventListener('click', () => deleteBook(bookId));
    })
  }

  function submit() {
    const title = inputBookTitle.value;
    const author = inputBookAuthor.value;
    let obj = { 'author': author, 'title': title };
    const headers = { 'Content-Type': 'application/json' };

    if (formTitle.textContent === 'Edit FORM' && title && author) {
      fetch(`${BASE_URL}${editBookId}`, {
        method: `PUT`,
        headers: headers,
        body: JSON.stringify(obj)
      })
        .then(loadBooks)
        .catch((err) => console.error(err));
    } else if (title && author) {
      fetch(BASE_URL, {
        method: `POST`,
        headers: headers,
        body: JSON.stringify(obj)
      })
        .then(loadBooks)
        .catch((err) => console.error(err));
    }
  }

  function deleteBook(id) {
    fetch(`${BASE_URL}${id}`, { method: 'DELETE' })
      .then(res => res.json())
      .then(loadBooks)
      .catch((err) => console.error(err));
  }
}

attachEvents();