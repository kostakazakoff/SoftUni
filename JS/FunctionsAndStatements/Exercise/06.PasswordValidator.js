function passwordValidator(password) {
    const regex1 = /\d{2,}/g;
    const regex2 = /[^A-z\d]/g;
    let valid = true;
    if (password.length < 6 || password.length > 10) {
        console.log('Password must be between 6 and 10 characters');
        valid = false;
    } if (password.match(regex2)) {
        console.log('Password must consist only of letters and digits');
        valid = false;
    } if (!password.match(regex1)) {
        console.log('Password must have at least 2 digits');
        valid = false;
    } if (valid) {
        console.log('Password is valid');
    }
}

// passwordValidator('Pa$s$s')