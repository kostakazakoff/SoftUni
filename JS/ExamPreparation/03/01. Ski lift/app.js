window.addEventListener('load', solve);

function solve() {
    const inputDomSelectors = {
        'fNameInput': document.getElementById('first-name'),
        'lNameInput': document.getElementById('last-name'),
        'peopleInput': document.getElementById('people-count'),
        'dateInput': document.getElementById('from-date'),
        'daysInput': document.getElementById('days-count')
    }
    const nextBtn = document.getElementById('next-btn');
    const firstForm = document.querySelector('#append-ticket form');
    const ticketPreviewList = document.querySelector('.ticket-info-list');
    const confirmTicketList = document.querySelector('.confirm-ticket');
    let ticketCasch = [];

    nextBtn.addEventListener('click', toTicketPreview);

    function toTicketPreview(e) {
        e?.preventDefault();

        const inputIsValid = Object.values(inputDomSelectors).every(field => field.value.length > 0);
        
        
        console.log(ticketCasch);
        if (!inputIsValid) { return };

        const li = createHTMLElement('li', ticketPreviewList);
        const article = createHTMLElement('article', li);
        createHTMLElement('h3', article, `Name: ${inputDomSelectors.fNameInput.value} ${inputDomSelectors.lNameInput.value}`);
        createHTMLElement('p', article, `From date: ${inputDomSelectors.dateInput.value}`);
        createHTMLElement('p', article, `For ${inputDomSelectors.daysInput.value} days`);
        createHTMLElement('p', article, `For ${inputDomSelectors.peopleInput.value} people`);
        const editBtn = createHTMLElement('button', li, 'Edit', ['edit-btn']);
        const continueBtn = createHTMLElement('button', li, 'Continue', ['continue-btn']);

        editBtn.addEventListener('click', editTask);
        continueBtn.addEventListener('click', toConfirmForm);
    }

    function editTask() {

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