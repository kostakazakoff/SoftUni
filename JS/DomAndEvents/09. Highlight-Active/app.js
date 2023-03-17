function focused() {
    Array.from(document.querySelectorAll('input'))
    .forEach(input => {
        input.addEventListener('focus', onFocus);
        input.addEventListener('blur', blur);
    })
    function onFocus() {
        console.log(this.parentElement);
        this.parentElement.className = 'focused';
    }
    function blur() {
        console.log(this.parentElement);
        this.parentElement.classList.remove('focused');
    }
}