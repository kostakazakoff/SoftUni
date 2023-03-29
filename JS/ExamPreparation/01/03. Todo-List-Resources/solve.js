function attachEvents() {
    const inputField = document.getElementById('title');
    const addBtn = document.getElementById('add-button');
    const loadBtn = document.getElementById('load-button');
    const todoList = document.getElementById('todo-list');
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/'

    addBtn.addEventListener('click', addNewTask);
    loadBtn.addEventListener('click', loadTasks);

    function loadTasks(event) {
        event?.preventDefault()

        fetch(BASE_URL)
            .then(response => response.json())
            .then(data => outputTasks(data))
            .catch(err => console.log(err));
    }

    function outputTasks(tasks) {
        inputField.value = '';
        todoList.innerHTML = '';

        Object.values(tasks).forEach(task => {
            const li = document.createElement('li');
            const span = document.createElement('span');
            const removeBtn = document.createElement('button');
            const editBtn = document.createElement('button');

            li.id = task._id;
            span.textContent = `${task.name}`;
            removeBtn.textContent = 'Remove';
            editBtn.textContent = 'Edit';
            removeBtn.addEventListener('click', removeTask);
            editBtn.addEventListener('click', editTask);

            [span, removeBtn, editBtn].forEach(el => li.appendChild(el));
            todoList.appendChild(li);
        })
    }

    function addNewTask(event) {
        event?.preventDefault();
        fetch(BASE_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 'name': inputField.value })
        })
            .then(() => loadTasks())
            .catch(err => console.log(err));
    }

    function removeTask(e) {
        const id = e.target.parentElement.id;
        fetch(`${BASE_URL}${id}`, { method: 'DELETE' })
            .then(() => loadTasks())
            .catch(err => console.log(err));
    }

    function editTask(event) {
        const id = event.target.parentElement.id;
        const task = event.currentTarget.parentElement;
        const [span, removeBtn, editBtn] = Array.from(task.children);

        const formInput = document.createElement('input');
        formInput.value = span.textContent;

        const submitBtn = document.createElement('button');
        submitBtn.textContent = 'Submit';

        task.innerHTML = '';
        task.appendChild(formInput);
        task.appendChild(removeBtn);
        task.appendChild(submitBtn);

        submitBtn.addEventListener('click', () => {
            const httpHeaders = {
                method: 'PATCH',
                body: JSON.stringify({ name: formInput.value })
            }
            fetch(`${BASE_URL}${id}`, httpHeaders)
                .then(() => loadTasks())
                .catch(err => console.log(err));
        });
    }
}

attachEvents();
