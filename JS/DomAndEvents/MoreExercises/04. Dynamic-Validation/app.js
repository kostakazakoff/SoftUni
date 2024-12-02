function validate() {
    const emailInputField = document.getElementById('email');
    emailInputField.addEventListener('change', validateInput);

    function validateInput() {
        const valid = emailInputField.value.match(/^[a-z]+\@[a-z]+\.[a-z]+$/g);
        if (!valid) {
            emailInputField.setAttribute('class', 'error')
        } else {
            emailInputField.removeAttribute('class');
        }
    }
}