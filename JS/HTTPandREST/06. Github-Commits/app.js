function loadCommits() {
    const usernameInput = document.getElementById('username');
    const repoInput = document.getElementById('repo');
    const outputField = document.getElementById('commits')
    const username = usernameInput.value;
    const repo = repoInput.value;
    const TARGET_URL = 'https://api.github.com/repos/'

    fetch(`${TARGET_URL}${username}/${repo}/commits`, { method: 'GET' })
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
            data.forEach(({ commit }) => {
                const li = document.createElement('li');
                li.textContent = `${commit.author.name}: ${commit.message}`;
                outputField.appendChild(li);
            });
        } else {
            const li = document.createElement('li');
            li.textContent = `${data} (Not Found)`;
            outputField.appendChild(li);
        }
    }
}