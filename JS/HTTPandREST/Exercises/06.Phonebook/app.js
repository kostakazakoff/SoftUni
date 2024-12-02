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

    function loadPhoneBook() {
        fetch(BASE_URL)
            .then((response) => response.json())
            .then((data) => outputData(data))
            .catch((err) => console.log(err))
    }

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

    function createContact() {
        const person = inputPerson.value;
        const phone = inputPhone.value;
        const obj = { 'person': person, 'phone': phone };
        const headers = { 'Content-Type': 'application/json' }

        fetch(BASE_URL, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(obj)
        })
            .then(() => {
                loadPhoneBook();
                inputPerson.value = '';
                inputPhone.value = '';
            })
            .catch((err) => console.error(err));
    }

    function deleteContact(id) {
        fetch(`${BASE_URL}${id}`, { method: 'DELETE' })
            .then(response => response.json())
            .then(loadPhoneBook)
            .catch((err) => console.error(err));
    }
}

attachEvents();