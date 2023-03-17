function toggle() {
    const btn = document.getElementsByClassName('button')[0];
    const div = document.getElementById('extra');
    if (btn.textContent === 'More') {
        div.style.display = 'block';
        btn.textContent = 'Less';
    } else {
        div.style.display = 'none';
        btn.textContent = 'More';
    }  
}