function readInput(input) {
    idx = 0;
    while(true) {
        let word = input[idx];
        if(word == "Stop"){
            break;
        }
        console.log(word);
        idx ++;
    }  
}

// readInput(["Nakov",
//         "SoftUni",
//         "Sofia",
//         "Bulgaria",
//         "SomeText",
//         "Stop",
//         "AfterStop",
//         "Europe",
//         "HelloWorld"])