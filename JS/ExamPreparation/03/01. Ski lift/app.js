window.addEventListener('load', solve);

function solve() {
    const inputDomSelectors = {
        fName: document.getElementById('first-name'),
        lName: document.getElementById('last-name'),
        people: document.getElementById('people-count'),
        date: document.getElementById('from-date'),
        days: document.getElementById('days-count')
    }
    const nextBtn = document.getElementById('next-btn');
    const firstForm = document.querySelector('#append-ticket form');
    const ticketPreviewList = document.querySelector('.ticket-info-list');
    const confirmTicketList = document.querySelector('.confirm-ticket');
    let ticketCasch = {};

    nextBtn.addEventListener('click', toTicketPreview);

    function toTicketPreview(e) {
        if (e) { e.preventDefault() };

        const inputIsValid = Object.values(inputDomSelectors).every(field => field.value.length > 0);
        if (!inputIsValid) { return };

        const { fName, lName, people, date, days } = inputDomSelectors;
        ticketCasch = {
            fName: fName.value,
            lName: lName.value,
            people: people.value,
            date: date.value,
            days: days.value
        }

        const li = createHTMLElement('li', ticketPreviewList);
        const article = createHTMLElement('article', li);
        createHTMLElement('h3', article, `Name: ${inputDomSelectors.fName.value} ${inputDomSelectors.lName.value}`);
        createHTMLElement('p', article, `From date: ${inputDomSelectors.date.value}`);
        createHTMLElement('p', article, `For ${inputDomSelectors.days.value} days`);
        createHTMLElement('p', article, `For ${inputDomSelectors.people.value} people`);

        const editBtn = createHTMLElement('button', li, 'Edit', ['edit-btn']);
        const continueBtn = createHTMLElement('button', li, 'Continue', ['continue-btn']);

        editBtn.addEventListener('click', editTask);
        continueBtn.addEventListener('click', toConfirmForm);

        firstForm.reset();
        nextBtn.disabled = true;
    }

    function editTask() {
        this.parentNode.remove();
        for (const key in ticketCasch) {
            inputDomSelectors[key].value = ticketCasch[key];
        }
        nextBtn.disabled = false;
    }

    function toConfirmForm() {
        const li = createHTMLElement('li', confirmTicketList);
        li.appendChild(this.parentNode.firstChild);

        const confirmBtn = createHTMLElement('button', li, 'Confirm', ['confirm-btn']);
        const cancelBtn = createHTMLElement('button', li, 'Cancel', ['cancel-btn']);

        this.parentNode.remove();

        confirmBtn.addEventListener('click', confirm);
        cancelBtn.addEventListener('click', cancel);
    }

    function confirm() {
        const bodyContainer = document.getElementById('body');
        bodyContainer.innerHTML = '';
        createHTMLElement('h1', bodyContainer, 'Thank you, have a nice day!', null, 'thank-you');
        const backBtn = createHTMLElement('button', bodyContainer, 'Back', null, 'back-btn');

        backBtn.addEventListener('click', () => window.location.reload());
    }

    function cancel() {
        this.parentNode.innerHTML = '';
        nextBtn.disabled = false;
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