function passwordCheck(input){
    let username = input[0];
    let password = input[1];
    let idx = 2;
    while(true){
        let password_try = input[idx];
        if(password_try === password){
            console.log(`Welcome ${username}!`);
            break;
        }
        idx++;
    }
}

// passwordCheck(["Nakov",
//             "1234",
//             "Pass",
//             "1324",
//             "1234"])