function lockedProfile() {
    Array.from(document.querySelectorAll('button'))
    .forEach(btn => {
        btn.addEventListener('click', toggleVisibility);
    })
    
    function toggleVisibility() {
        const hiddenContent = this.parentElement.querySelector('div');
        const radioBtnLock = this.parentElement.querySelectorAll('input[type="radio"]')[0];
        if (this.textContent === 'Show more' && !radioBtnLock.checked) {
            hiddenContent.style.display = 'block';
            this.textContent = 'Hide it';
        } else if (this.textContent === 'Hide it' && !radioBtnLock.checked) {
            hiddenContent.style.display = 'none';
            this.textContent = 'Show more';
        }
    }
}