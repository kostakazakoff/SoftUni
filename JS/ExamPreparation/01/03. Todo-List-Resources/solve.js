function attachEvents() {
    const inputField = document.getElementById('title');
    const addBtn = document.getElementById('add-button');
    const loadBtn = document.getElementById('load-button');
    const todoList = document.getElementById('todo-list');
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/'

    addBtn.addEventListener('click', () => addTask())

    loadTasks()

    function loadTasks() {
        fetch(BASE_URL)
            .then(response => response.json())
            .then(data => outputTasks(data))
            .catch(err => console.log(err));
    }

    function outputTasks(data) {
        inputField.value = '';
        todoList.innerHTML = '';

        Object.values(data).forEach(task => {
            const li = document.createElement('li');
            const span = document.createElement('span');
            const removeBtn = document.createElement('button');
            const editBtn = document.createElement('button');

            li.id = task._id;
            span.textContent = `${task.name}`;
            removeBtn.textContent = 'Remove';
            editBtn.textContent = 'Edit';
            removeBtn.addEventListener('click', () => removeTask(task._id));
            editBtn.addEventListener('click', () => editTask(task._id));

            [span, removeBtn, editBtn].forEach(el => li.appendChild(el));
            todoList.appendChild(li);
        })
    }

    function addTask() {
        const title = inputField.value;
        const headers = { 'Content-Type': 'application/json' };
        fetch(BASE_URL, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify({ 'name': title })
        })
            .then(() => loadTasks())
            .catch(err => console.log(err));
    }

    function removeTask(id) {
        fetch(`${BASE_URL}${id}`, { method: 'DELETE' })
            .then(() => loadTasks())
            .catch(err => console.log(err));
    }

    function editTask(id) {
        console.log('Edit');
    }
}

attachEvents();
