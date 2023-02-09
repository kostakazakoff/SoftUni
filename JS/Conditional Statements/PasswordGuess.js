function checkPassword(params) {
    let password = "s3cr3t!P@ssw0rd";
    let input = params[0];
    if (input == password) {console.log("Welcome")}
    else {console.log("Wrong password!")}
}