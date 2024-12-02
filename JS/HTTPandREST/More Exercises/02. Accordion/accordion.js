function solution() {
    const mainContainer = document.getElementById('main');
    const LEADS_URL = 'http://localhost:3030/jsonstore/advanced/articles/list/';
    const CONTENT_URL = 'http://localhost:3030/jsonstore/advanced/articles/details/';

    fetch(LEADS_URL)
        .then(res => res.json())
        .then(data => handleLeads(data))
        .catch(err => console.log(err));

    function handleLeads(leads) {
        leads.forEach(lead => {
            const div = document.createElement('div');
            div.className = 'accordion';
            const id = lead._id

            div.innerHTML = `
            <div class="head">
                <span>${lead.title}</span>
                <button class="button" id="${id}">More</button>
            </div>
            <div class="extra" name="${id}"></div>
            `;

            mainContainer.appendChild(div);
            document.getElementById(`${id}`).addEventListener('click', loadContent(id))
        });

        function loadContent(id) {
            fetch(`${CONTENT_URL}${id}`)
                .then(res => res.json())
                .then(data => addContent(data))
                .catch(err => console.log(err))
        }

        function addContent(data) {
            const btn = document.getElementById(`${data._id}`);
            const content = data.content;
            const contentBox = document.querySelector(`div[name="${data._id}"`)
            const p = document.createElement('p');
            p.textContent = content;
            contentBox.appendChild(p);

            btn.addEventListener('click', () => {
                if (btn.textContent === 'More') {
                    contentBox.style.display = 'block';
                    btn.textContent = 'Less';
                } else {
                    contentBox.style.display = 'none';
                    btn.textContent = 'More';
                }
            })
        }
    }
}


solution()