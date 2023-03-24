function attachEvents() {
    const loadBtn = document.getElementById('btnLoad');
    const createBtn = document.getElementById('btnCreate');
    const inputPerson = document.getElementById('person');
    const inputPhone = document.getElementById('phone');
    const phonebookUL = document.getElementById('phonebook');
    // const fragment = new DocumentFragment();

    const BASE_URL = 'http://localhost:3030/jsonstore/phonebook/';

    loadBtn.addEventListener('click', loadPhoneBook);
    createBtn.addEventListener('click', createContact);

    function outputData(data) {
        phonebookUL.textContent = '';
        Object.values(data).forEach(v => {
            const li = document.createElement('li');
            const deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Delete';
            li.id = v._id;
            li.textContent = `${v.person}: ${v.phone}`
            deleteBtn.addEventListener('click', () => deleteContact(v._id))
            li.appendChild(deleteBtn);
            phonebookUL.appendChild(li);
            // fragment.appendChild(li);
        })
        // phonebookUL.appendChild(fragment);
    }

    function loadPhoneBook() {
        fetch(BASE_URL)
            .then((response) => response.json())
            .then((data) => outputData(data))
            .catch((err) => console.log(err))
    }

    function createContact() {
        const person = inputPerson.value;
        const phone = inputPhone.value;
        const obj = { 'person': person, 'phone': phone };
        fetch(BASE_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(obj)
        })
            .then(response => { loadPhoneBook() })
            .catch((err) => console.error(err));
        inputPerson.value = '';
        inputPhone.value = '';
    }

    function deleteContact(id) {
        fetch(`${BASE_URL}${id}`, { method: 'DELETE' })
            .then(response => response.json())
            .then(data => console.log(data))
            .then(data => loadPhoneBook())
            .catch((err) => console.error(err));
    }
}

attachEvents();