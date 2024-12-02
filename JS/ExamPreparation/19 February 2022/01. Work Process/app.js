function solve() {
    const firstName = document.getElementById('fname');
    const lastName = document.getElementById('lname');
    const email = document.getElementById('email');
    const birth = document.getElementById('birth');
    const position = document.getElementById('position');
    const salary = document.getElementById('salary');

    const hireBtn = document.getElementById('add-worker');
    hireBtn.addEventListener('click', addWorker);

    const hiredWorkersList = document.getElementById('tbody');
    const budgetMessage = document.getElementById('sum');
    let salariesSum = 0;

    function addWorker(e) {
        if (e) { e.preventDefault(); };

        validInput = [firstName, lastName, email, birth, position, salary].every(f => f.value.length > 0);
        if (!validInput) { return; };

        const tr = createHTMLElement('tr', hiredWorkersList);
        createHTMLElement('td', tr, firstName.value);
        createHTMLElement('td', tr, lastName.value);
        createHTMLElement('td', tr, email.value);
        createHTMLElement('td', tr, birth.value);
        createHTMLElement('td', tr, position.value);
        createHTMLElement('td', tr, salary.value);
        const td = createHTMLElement('td', tr);
        const firedBtn = createHTMLElement('button', td, 'Fired', ['fired']);
        const editBtn = createHTMLElement('button', td, 'Edit', ['edit']);

        firedBtn.addEventListener('click', fireWorker);
        editBtn.addEventListener('click', editWorkerInfo);

        salariesSum += parseFloat(salary.value);
        budgetMessage.textContent = salariesSum.toFixed(2);

        [firstName, lastName, email, birth, position, salary].map(f => f.value = '');
    }

    function fireWorker() {
        salariesSum -= parseFloat(this.parentNode.parentNode.querySelector('td:nth-child(6)').textContent);
        budgetMessage.textContent = salariesSum.toFixed(2);
        this.parentNode.parentNode.remove();
    }

    function editWorkerInfo() {
        firstName.value = this.parentNode.parentNode.querySelector('td:nth-child(1)').textContent;
        lastName.value = this.parentNode.parentNode.querySelector('td:nth-child(2)').textContent;
        email.value = this.parentNode.parentNode.querySelector('td:nth-child(3)').textContent;
        birth.value = this.parentNode.parentNode.querySelector('td:nth-child(4)').textContent;
        position.value = this.parentNode.parentNode.querySelector('td:nth-child(5)').textContent;
        salary.value = this.parentNode.parentNode.querySelector('td:nth-child(6)').textContent;

        salariesSum -= parseFloat(salary.value);
        budgetMessage.textContent = salariesSum.toFixed(2);

        this.parentNode.parentNode.remove();
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
solve()