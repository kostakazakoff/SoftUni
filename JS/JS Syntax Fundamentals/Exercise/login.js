function login(arr){
    let username = arr[0];
    let passwords = arr.slice(1)
    let counter = 0;
    for (let i = 0; i < passwords.length; i++){
        counter ++;
        let pwd = passwords[i];
        pwd = pwd.split('').reverse(pwd).join('');
        if (username === pwd){
            console.log(`User ${username} logged in.`);
            break;
        } if (counter === 4){
            console.log(`User ${username} blocked!`);
            break;
        } else {
            console.log('Incorrect password. Try again.');
        };
    }
}

// login(['sunny','rainy','cloudy','sunny','not sunny'])