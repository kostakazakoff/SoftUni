function loadRepos() {
    let username = document.getElementById('input-username');
    fetch(`https://api.github.com/users/${kostakazakoff}/repos`)
        .then(res => res.json())
        .then(handleResponse)
        .catch(err => console.log(err));
}

function handleResponse(data) {
    console.log(data);
}

// loadRepos()
