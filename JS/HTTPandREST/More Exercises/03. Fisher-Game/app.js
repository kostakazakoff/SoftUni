function solution() {
    localStorage.setItem('userInfo', {"email": "george@abv.bg", "password": "123456"})
    const LOGIN_URL = 'http://localhost:3030/users/login'
    let userCredentials = localStorage.getItem('userinfo')

    fetch(LOGIN_URL, {
        method: 'POST',
        headers: {"content-type": "application/json"},
        body: JSON.stringify(userCredentials)
    })
    .then(registerUser())
    .catch(error => console.error(error))


    function registerUser() {
        alert('Registration')
    }
}

solution()