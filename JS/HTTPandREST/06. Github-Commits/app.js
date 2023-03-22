function loadCommits() {
    const usernameInput = document.getElementById('username');
    const repoInput = document.getElementById('repo');
    const outputField = document.getElementById('commits')
    const TARGET_URL = `https://api.github.com/repos/${usernameInput.value}/${repoInput.value}/commits`

    fetch(TARGET_URL, { method: 'GET' })
        .then((response) => checkError(response))
        .then((response) => response.json())
        .then((data) => createOutput(data))
        .catch((error) => createOutput(error))

    function checkError(response) {
        if (response.status >= 200 && response.status < 300) {
            return response;
        } else {
            throw Error(response.status);
        }
    }

    function createOutput(data) {
        outputField.textContent = '';
        if (data.length > 0) {
            Object.values(data).forEach(v => {
                const li = document.createElement('li');
                li.textContent = `${v['commit']['author']['name']}: ${v['commit']['message']}`;
                outputField.appendChild(li)
            });
        } else {
            const li = document.createElement('li');
                li.textContent = `${data} (Not Found)`;
                outputField.appendChild(li)
        }
        
    }
}