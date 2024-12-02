function sprintReview(arr) {
    const n = parseInt(arr.shift());

    const assigneesInfo = arr.slice(0, n);
    const allCommands = arr.slice(n);
    let assigneesList = {};

    assigneesInfo.forEach(a => {
        let [assignee, taskId, title, status, estimatedPoints] = a.split(':');
        if (!assigneesList.hasOwnProperty(assignee)) {
            assigneesList[assignee] = [];
        }
        assigneesList[assignee].push({ taskId, title, status, estimatedPoints });
    });

    const execute = {
        'Add New': addNew,
        'Change Status': changeStatus,
        'Remove Task': removeTask
    }

    allCommands.forEach(commandLine => {
        const [command, ...args] = commandLine.split(':');
        execute[command](args);
    });

    function addNew(task) {
        const [assignee, taskId, title, status, estimatedPoints] = task;
        if (!assigneesList.hasOwnProperty(assignee)) {
            console.log(`Assignee ${assignee} does not exist on the board!`);
            return;
        }
        assigneesList[assignee].push({ assignee, taskId, title, status, estimatedPoints });
    }

    function changeStatus(args) {
        const [assignee, taskId, newStatus] = args;
        if (!assigneesList.hasOwnProperty(assignee)) {
            console.log(`Assignee ${assignee} does not exist on the board!`);
            return;
        }
        for (const task of assigneesList[assignee]) {
            if (task.taskId === taskId) {
                task.status = newStatus;
                return;
            }
        }
        console.log(`Task with ID ${taskId} does not exist for ${assignee}!`)
    }

    function removeTask(args) {
        const [assignee, index] = args;
        const indexNum = parseInt(index);
        
        if (!assigneesList.hasOwnProperty(assignee)) {
            console.log(`Assignee ${assignee} does not exist on the board!`);
            return;
        }

        if (assigneesList[assignee].length <= indexNum) {
            console.log(`Index is out of range!`);
            return;
        }
        assigneesList[assignee].splice(index, 1);
    }

    let toDoTasksTotalPoints = 0;
    let inProgressTasksTotalPoints = 0;
    let codeReviewTasksTotalPoints = 0;
    let doneTasksTotalPoints = 0;

    Object.values(assigneesList).forEach(a => {
        a.forEach(task => {
            if (task.status === 'ToDo') { toDoTasksTotalPoints += parseInt(task.estimatedPoints) }
            else if (task.status === 'In Progress') { inProgressTasksTotalPoints += parseInt(task.estimatedPoints) }
            else if (task.status === 'Code Review') { codeReviewTasksTotalPoints += parseInt(task.estimatedPoints) }
            else if (task.status === 'Done') { doneTasksTotalPoints += parseInt(task.estimatedPoints) }
        });
    });

    console.log(`ToDo: ${toDoTasksTotalPoints}pts`);
    console.log(`In Progress: ${inProgressTasksTotalPoints}pts`);
    console.log(`Code Review: ${codeReviewTasksTotalPoints}pts`);
    console.log(`Done Points: ${doneTasksTotalPoints}pts`);

    const successfull = doneTasksTotalPoints >= toDoTasksTotalPoints + inProgressTasksTotalPoints + codeReviewTasksTotalPoints;

    if (successfull) {
        console.log('Sprint was successful!');
    } else {
        console.log('Sprint was unsuccessful...');
    }
}



sprintReview(
    [
        '5',
        'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
        'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
        'Peter:BOP-1211:POC:Code Review:5',
        'Georgi:BOP-1212:Investigation Task:Done:2',
        'Mariya:BOP-1213:New Account Page:In Progress:13',
        'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
        'Change Status:Peter:BOP-1290:ToDo',
        'Remove Task:Mariya:1',
        'Remove Task:Joro:1',
    ]
)