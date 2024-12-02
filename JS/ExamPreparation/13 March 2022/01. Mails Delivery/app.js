function solve() {
    const form = document.querySelector('form');
    const name = document.getElementById('recipientName');
    const title = document.getElementById('title');
    const message = document.getElementById('message');

    const addBtn = document.getElementById('add');
    const resetBtn = document.getElementById('reset');

    const listOfMails = document.getElementById('list');
    const sentMails = document.querySelector('.sent-list');
    const deletedMails = document.querySelector('.delete-list');

    addBtn.addEventListener('click', addToListOfMails);
    resetBtn.addEventListener('click', resetMail);

    function addToListOfMails(e) {
        if (e) { e.preventDefault() };

        const validInput = [name, title, message].every(f => f.value.length > 0);
        if (!validInput) { return };

        const li = createHTMLElement('li', listOfMails);
        createHTMLElement('h4', li, `Title: ${title.value}`);
        createHTMLElement('h4', li, `Recipient Name: ${name.value}`);
        createHTMLElement('span', li, message.value);
        const div = createHTMLElement('div', li, null, null, 'list-action');
        const sendBtn = createHTMLElement('button', div, 'Send', null, 'send', {'type': 'submit'});
        const deleteBtn = createHTMLElement('button', div, 'Delete', null, 'delete', {'type': 'submit'});

        resetMail();

        sendBtn.addEventListener('click', sendMail);
        deleteBtn.addEventListener('click', deleteMail);
    }

    function resetMail(e) {
        if (e) {e.preventDefault()};
        [name, title, message].map(f => f.value = '');
    }

    function sendMail() {        
        console.log(this.parentNode.parentNode.querySelector('h4'))
        const li = createHTMLElement('li', sentMails);
        createHTMLElement('span', li, `To: ${this.parentNode.parentNode.querySelectorAll('h4')[1].textContent.split(': ')[1]}`);
        createHTMLElement('span', li, `${this.parentNode.parentNode.querySelectorAll('h4')[0].textContent}`);
        const div = createHTMLElement('div', li, null, ['btn']);
        const deleteBtn = createHTMLElement('button', div, 'Delete', ['delete'], null, {'type': 'submit'});

        deleteBtn.addEventListener('click', deleteSentMail)

        this.parentNode.parentNode.remove();
    }

    function deleteMail() {
        const li = createHTMLElement('li', deletedMails);
        createHTMLElement('span', li, `To: ${this.parentNode.parentNode.querySelectorAll('h4')[1].textContent.split(': ')[1]}`);
        createHTMLElement('span', li, `${this.parentNode.parentNode.querySelectorAll('h4')[0].textContent}`);

        this.parentNode.parentNode.remove();
    }

    function deleteSentMail() {
        deletedMails.appendChild(this.parentNode.parentNode);
        deletedMails.querySelector('div').remove();
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