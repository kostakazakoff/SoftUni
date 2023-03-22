function loadRepos() {
	const inputUsername = document.getElementById('username').value;
	const outputUL = document.getElementById('repos');
	const URL = `https://api.github.com/users/${inputUsername}/repos`

	fetch (URL, {method: 'GET'})
	.then((response) => checkError(response))
	.then((response) => response.json())
	.then((data) => parseData(data))
	.catch((err) => {
		outputUL.textContent = '';
		createLi(err);
	})

	function checkError(response) {
		if (response.status >= 200 && response.status < 300) {
			return response;
		} else {
			throw Error(response.status);
		}
	}

	function createLi(input) {
		const li = document.createElement('li');
			const a = document.createElement('a');
			if (input === 'err'){
				a.href = '#'
			} else {
				a.href = input;
			}
			a.textContent = input;
			li.appendChild(a);
			outputUL.appendChild(li);
	}

	function parseData(data) {
		outputUL.textContent = '';
		data.forEach(d => {
			createLi(d["full_name"])
		});
	}
}