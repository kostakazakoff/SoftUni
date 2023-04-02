window.addEventListener('load', solve);

function solve() {
    let caschedInfo = {};
    const inputForm = document.querySelector('form');
    const verification = document.getElementById('verification')
    const inputDOMSelectors = {
        firstName: document.getElementById('first-name'),
        lastName: document.getElementById('last-name'),
        checkIn: document.getElementById('date-in'),
        checkOut: document.getElementById('date-out'),
        guests: document.getElementById('people-count'),
    };
    const nextBtn = document.getElementById('next-btn');

    const infoList = document.querySelector('.info-list');
    const confirmList = document.querySelector('.confirm-list');

    nextBtn.addEventListener('click', toInfoList);

    function parseDate(date) {
        const year = parseInt(date.substring(0, 4));
        const month = parseInt(date.substring(5, 7));
        const day = parseInt(date.substring(8, 10));
        const dateObj = new Date(year, month, day);
        return dateObj;
    }

    function toInfoList(e) {
        if (e) { e.preventDefault() }

        const chkIn = parseDate(inputDOMSelectors.checkIn.value);
        const chkOut = parseDate(inputDOMSelectors.checkOut.value);

        const inputIsValid = Object.values(inputDOMSelectors)
            .every(field => field.value.length > 0) && chkIn < chkOut;

        if (!inputIsValid) { return };

        const { firstName, lastName, checkIn, checkOut, guests } = inputDOMSelectors;
        caschedInfo = {
            firstName: firstName.value,
            lastName: lastName.value,
            checkIn: checkIn.value,
            checkOut: checkOut.value,
            guests: guests.value
        };

        const li = createHTMLElement('li', infoList, null, ['reservation-content']);
        const article = createHTMLElement('article', li);
        createHTMLElement('h3', article, `Name: ${caschedInfo.firstName} ${caschedInfo.lastName}`);
        createHTMLElement('p', article, `From date: ${caschedInfo.checkIn}`);
        createHTMLElement('p', article, `To date: ${caschedInfo.checkOut}`);
        createHTMLElement('p', article, `For ${caschedInfo.guests} people`);
        const editBtn = createHTMLElement('button', li, 'Edit', ['edit-btn']);
        const continueBtn = createHTMLElement('button', li, 'Continue', ['continue-btn']);

        editBtn.addEventListener('click', backToInput)
        continueBtn.addEventListener('click', toConfirm);

        nextBtn.disabled = true;
        inputForm.reset()
    }

    function backToInput() {
        for (const key in caschedInfo) {
            inputDOMSelectors[key].value = caschedInfo[key];
        }

        this.parentNode.remove();
        nextBtn.disabled = false;
    }

    function toConfirm() {
        const li = createHTMLElement('li', confirmList)
        li.appendChild(this.parentNode.firstChild);
        this.parentNode.remove();

        const confirmBtn = createHTMLElement('button', li, 'Confirm', ['confirm-btn']);
        const cancelBtn = createHTMLElement('button', li, 'Cancel', ['cancel-btn']);

        confirmBtn.addEventListener('click', confirm);
        cancelBtn.addEventListener('click', cancel);
    }

    function confirm() {
        this.parentNode.remove();
        createHTMLElement('h1', verification, 'Confirmed.', ['reservation-confirmed']);
        nextBtn.disabled = false;
    }

    function cancel() {
        this.parentNode.remove();
        createHTMLElement('h1', verification, 'Cancelled.', ['reservation-cancelled']);
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





