window.addEventListener('load', solve);

function solve() {
    const genreInput = document.getElementById('genre');
    const nameInput = document.getElementById('name');
    const authorInput = document.getElementById('author');
    const dateInput = document.getElementById('date');
    const addBtn = document.getElementById('add-btn');
    const imgSource = './static/img/img.png'
    const allHitsContainer = document.querySelector('.all-hits-container');
    const savedContainer = document.querySelector('.saved-container');
    const totalLikesField = document.querySelector('.likes > p');
    let likes = 0;

    addBtn.addEventListener('click', addSong);

    function addSong(e) {
        e.preventDefault();
        
        const validInput = [genreInput, nameInput, authorInput, dateInput].every(field => field.value.length > 0);
        if (!validInput) { return };

        const div = createHTMLElement('div', allHitsContainer, null, ['hits-info']);
        createHTMLElement('img', div, null, null, null, { src: imgSource });
        createHTMLElement('h2', div, `Genre: ${genreInput.value}`);
        createHTMLElement('h2', div, `Name: ${nameInput.value}`);
        createHTMLElement('h2', div, `Author: ${authorInput.value}`);
        createHTMLElement('h3', div, `Date: ${dateInput.value}`);

        const saveBtn = createHTMLElement('button', div, 'Save song', ['save-btn']);
        const likeBtn = createHTMLElement('button', div, 'Like song', ['like-btn']);
        const deleteBtn = createHTMLElement('button', div, 'Delete', ['delete-btn']);

        document.querySelector('form').reset();

        saveBtn.addEventListener('click', saveSong);
        likeBtn.addEventListener('click', incrementLikes);
        deleteBtn.addEventListener('click', deleteSong);
    }

    function incrementLikes() {
        likes++;
        totalLikesField.textContent = `Total Likes: ${likes}`
        this.disabled = true;
    }

    function saveSong() {
        const parent = this.parentNode;
        saveBtn = parent.querySelector('.save-btn');
        likeBtn = parent.querySelector('.like-btn');
        saveBtn.remove();
        likeBtn.remove();
        savedContainer.appendChild(parent);
    }

    function deleteSong() {
        this.parentNode.remove();
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