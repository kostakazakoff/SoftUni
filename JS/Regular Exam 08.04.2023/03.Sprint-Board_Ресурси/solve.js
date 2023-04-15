// TODO:
function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/';
    const todoSection = document.getElementById('todo-section');
    const inProgressSection = document.getElementById('in-progress-section');
    const codeReviewSection = document.getElementById('code-review-section');
    const doneSection = document.getElementById('done-section');

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

    function addTasksToTables(data) {
        Object.values(data).forEach(task => addTaskTo);
    }

    function addTaskTo(task) {
        const status = task.status;
        // const section = 
    }

    function createTask() {
        // TODO:
    }
}

attachEvents();