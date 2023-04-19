function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/';
    const todoSection = document.getElementById('todo-section');
    const inProgressSection = document.getElementById('in-progress-section');
    const codeReviewSection = document.getElementById('code-review-section');
    const doneSection = document.getElementById('done-section');

    const addForm = document.querySelector('form');
    const title = document.getElementById('title');
    const description = document.getElementById('description');

    const loadBoardBtn = document.getElementById('load-board-btn');
    const createTaskBtn = document.getElementById('create-task-btn');

    loadBoardBtn.addEventListener('click', loadAll);
    createTaskBtn.addEventListener('click', createTask);

    function loadAll() {
        fetch(BASE_URL)
            .then(res => res.json())
            .then(data => addTasksToTables(data))
            .catch(err => console.error(err));
    }

    function resetTables() {
        todoSection.querySelector('.task-list').innerHTML = '';
        inProgressSection.querySelector('.task-list').innerHTML = '';
        codeReviewSection.querySelector('.task-list').innerHTML = '';
        doneSection.querySelector('.task-list').innerHTML = '';
    }

    function addTasksToTables(data) {
        resetTables();
        Object.values(data).forEach(task => moveTaskTo(task));
    }

    function moveTaskTo(task) {
        const status = task.status;
        const position = {
            'ToDo': { 'parent': todoSection.querySelector('.task-list'), 'btnTextContent': 'Move to In Progress' },
            'In Progress': { 'parent': inProgressSection.querySelector('.task-list'), 'btnTextContent': 'Move to Code Review' },
            'Code Review': { 'parent': codeReviewSection.querySelector('.task-list'), 'btnTextContent': 'Move to Done' },
            'Done': { 'parent': doneSection.querySelector('.task-list'), 'btnTextContent': 'Close' },
        };
        const li = createHTMLElement('li', position[status].parent, null, ['task'], task._id);
        createHTMLElement('h3', li, task.title);
        createHTMLElement('p', li, task.description);
        const TaskBtn = createHTMLElement('button', li, position[status].btnTextContent);
        TaskBtn.addEventListener('click', handleTask);
    }

    function handleTask() {
        const id = this.parentNode.id;
        const section = this.parentNode.parentNode.parentNode.id;
        if (section === 'done-section') {
            deleteTask(id);
            return;
        }
        const nextStatus = {
            'todo-section': 'In Progress',
            'in-progress-section': 'Code Review',
            'code-review-section': 'Done'
        }
        const patchHeaders = {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 'status': nextStatus[section] })
        }
        fetch(`${BASE_URL}${id}`, patchHeaders)
        .then(loadAll)
        .catch(error => console.error(error));
    }

    function createTask() {
        // const inputIsValid = [title, description].every(field => field.value.length > 0);
        // if (!inputIsValid) {return;};
        const newTask = { 'title': title.value, 'description': description.value, 'status': 'ToDo' };
        const postHeaders = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newTask)
        }
        fetch(`${BASE_URL}`, postHeaders)
            .then(addForm.reset())
            .then(loadAll)
            .catch(err => console.error(err));
    }

    function deleteTask(id) {
        const deleteHeaders = {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
        }
        fetch(`${BASE_URL}${id}`, deleteHeaders)
            .then(loadAll)
            .catch(error => console.error(error));
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

attachEvents();