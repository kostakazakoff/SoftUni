function solution() {
    const mainContainer = document.getElementById('main');
    const LEADS_URL = 'http://localhost:3030/jsonstore/advanced/articles/list/';
    const CONTENT_URL = 'http://localhost:3030/jsonstore/advanced/articles/details/';
    let contentCasch = {};

    fetch(CONTENT_URL)
        .then(res => res.json())
        .then(data => contentCasch = data)
        .catch(err => console.log(err))

    fetch(LEADS_URL)
        .then(res => res.json())
        .then(data => handleLeads(data))
        .catch(err => console.log(err));

    function handleLeads(leads) {
        leads.forEach(lead => {
            const div = document.createElement('div');
            div.className = 'accordion';

            div.innerHTML = `
            <div class="head">
                <span>${lead.title}</span>
                <button class="button" id="${lead._id}">More</button>
            </div>
            <div class="extra">
            <p>${contentCasch[lead._id].content}</p>
            </div>
            `;

            mainContainer.appendChild(div);

            const btn = document.getElementById(`${lead._id}`)
            const contentBox = div.querySelector('.extra')
            
            btn.addEventListener('click', () => {
                if (btn.textContent === 'More') {
                    contentBox.style.display = 'block';
                    btn.textContent = 'Less';
                } else {
                    contentBox.style.display = 'none';
                    btn.textContent = 'More';
                }
            })
        });
    }
}

solution()