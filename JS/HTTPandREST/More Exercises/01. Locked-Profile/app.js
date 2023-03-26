function lockedProfile() {
    const mainContainer = document.getElementById('main');
    const fragment = new DocumentFragment();
    while (mainContainer.firstChild) { mainContainer.removeChild(mainContainer.lastChild); }

    let allProfiles = {};
    fetch('http://localhost:3030/jsonstore/advanced/profiles')
        .then(res => res.json())
        .then(data => { allProfiles = data; handleData() })
        .catch(err => console.log(err));

    function handleData() {
        Object.values(allProfiles).forEach(profile => {
            let username = profile.username;
            let email = profile.email;
            let age = profile.age;

            const newDiv = document.createElement('div');
            newDiv.className = "profile"
            newDiv.innerHTML = `
				<img src="./iconProfile2.png" class="userIcon" />
				<label>Lock</label>
				<input type="radio" name="${username}Locked" value="lock" checked>
				<label>Unlock</label>
				<input type="radio" name="${username}Locked" value="unlock"><br>
				<hr>
				<label>Username</label>
				<input type="text" name="${username}Username" value="${username}" disabled readonly />
				<div id="${username}HiddenFields" class="hiddenInfo">
					<hr>
					<label>Email:</label>
					<input type="email" name="${username}Email" value="${email}" disabled readonly />
					<label>Age:</label>
					<input type="text" name="${username}Age" value="${age}" disabled readonly />
				</div>
				
				<button>Show more</button>
            `;
            newDiv.querySelector('button').addEventListener('click', () => handleShowHideBtn(username))
            fragment.appendChild(newDiv);
        })
        mainContainer.appendChild(fragment);
    }

    function handleShowHideBtn(username) {
        const hiddenInfo = document.querySelector(`#${username}HiddenFields`);
        const profileCard = hiddenInfo.parentElement;
        const lockBtn = profileCard.querySelector('input')
        const showHideBtn = profileCard.querySelector('button')

        if (showHideBtn.textContent === 'Show more' && !lockBtn.checked) {
            hiddenInfo.removeAttribute('class')
            showHideBtn.textContent = 'Hide it';
        } else if (showHideBtn.textContent === 'Hide it' && !lockBtn.checked) {
            hiddenInfo.className = 'hiddenInfo'
            showHideBtn.textContent = 'Show more';
        }
    }
}