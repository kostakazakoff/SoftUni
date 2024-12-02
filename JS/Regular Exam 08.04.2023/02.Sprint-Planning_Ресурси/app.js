window.addEventListener('load', solve);

function solve() {
    let currId = 0;
    let totalPointsValue = 0;
    const totalPoints = document.getElementById('total-sprint-points');
    const inputForm = document.getElementById('create-task-form');
    const taskSection = document.getElementById('tasks-section')
    const taskId = document.getElementById('task-id');
    const title = document.getElementById('title');
    const description = document.getElementById('description');
    const label = document.getElementById('label');
    const points = document.getElementById('points');
    const assignee = document.getElementById('assignee');

    const createBtn = document.getElementById('create-task-btn');
    const deleteBtn = document.getElementById('delete-task-btn');

    createBtn.addEventListener('click', createTask);
    deleteBtn.addEventListener('click', deleteTask);

    const labelClasses = {
        'Feature': 'feature',
        'Low Priority Bug': 'low-priority',
        'High Priority Bug': 'high-priority'
    }

    const labelIcons = {
        'Feature': '&#8865',
        'Low Priority Bug': '&#9737',
        'High Priority Bug': '&#9888'
    }

    function createTask() {
        const inputIsValid = [title, description, points, assignee]
        .every(field => field.value.length > 0);

        if (!inputIsValid) { return }

        currId++;
        let id = `task-${currId}`;
        const labelValue = label.value;
        const labelClass = labelClasses[labelValue];
        const labelIcon = labelIcons[labelValue];
        const labelContent = `${label.value} ${labelIcon}`;
        const pointsContent = `Estimated at ${points.value} pts`;
        const assigneeContent = `Assigned to: ${assignee.value}`;

        const article = createHTMLElement('article', taskSection, null, ['task-card'], id);
        createHTMLElement('div', article, labelContent, ['task-card-label', labelClass], null, null, true);
        createHTMLElement('h3', article, title.value, ['task-card-title']);
        createHTMLElement('p', article, description.value, ['task-card-description']);
        createHTMLElement('div', article, pointsContent, ['task-card-points']);
        createHTMLElement('div', article, assigneeContent, ['task-card-assignee']);
        const btnsDiv = createHTMLElement('div', article, null, ['task-card-actions']);
        const deleteBtn = createHTMLElement('button', btnsDiv, 'Delete');

        totalPointsValue += parseInt(points.value);
        totalPoints.textContent = `Total Points ${totalPointsValue}pts`

        inputForm.reset();

        deleteBtn.addEventListener('click', prepareForDelete);
    }

    function prepareForDelete() {
        taskId.value = this.parentNode.parentNode.id;
        title.value = this.parentNode.parentNode.querySelector('.task-card-title').textContent;
        description.value = this.parentNode.parentNode.querySelector('.task-card-description').textContent;

        let lValue = this.parentNode.parentNode.querySelector('.task-card-label').textContent;
        lValue = lValue.split(' ');
        lValue = lValue.splice(0, lValue.length - 1);
        lValue = lValue.join(' ');

        label.value = lValue;
        points.value = this.parentNode.parentNode.querySelector('.task-card-points').textContent.split(' ')[2];
        assignee.value = this.parentNode.parentNode.querySelector('.task-card-assignee').textContent.split(': ')[1];
        
        createBtn.disabled = true;
        deleteBtn.disabled = false;

        [title, description, label, points, assignee].map(f => f.disabled = true);

    }

    function deleteTask() {
        const id = taskId.value;
        let taskToDel = document.querySelector(`#${id}`);

        totalPointsValue -= parseInt(points.value);
        totalPoints.textContent = `Total Points ${totalPointsValue}pts`

        taskToDel.remove();
        inputForm.reset();
        [title, description, label, points, assignee].map(f => f.disabled = false);
        

        createBtn.disabled = false;
        deleteBtn.disabled = true;
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