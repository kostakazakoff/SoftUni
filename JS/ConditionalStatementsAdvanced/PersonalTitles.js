function personalTitles(input) {
    let output = ''
    let age = Number(input[0]);
    let gender = input[1];

    switch (gender) {
        case ('m'):
            if (age < 16) {
                output = 'Master';
            } else {
                output = 'Mr.';
            }
            break;
        case ('f'):
            if (age < 16) {
                output = 'Miss';
            } else {
                output = 'Ms.';
            }
            break;  
    }
    console.log(output);
}


// function personalTitles(input) {
//     let output = ''
//     let age = Number(input[0]);
//     let gender = input[1];

//     if (gender == 'm') {
//         if (age < 16) {
//             output = 'Master';
//         }
//         else {
//             output = 'Mr.';
//         }
//     } else if (gender == 'f') {
//         if (age < 16) {
//             output = 'Miss';
//         }
//         else {
//             output = 'Ms.';
//         }
//     }

//     console.log(output);
// }

// function personalTitles(input) {
//     let age = Number(input[0]);
//     let gender = input[1];
//     let master = age < 16 & gender == 'm';
//     let mr = age >= 16 & gender == 'm';
//     let miss = age < 16 & gender == 'f';
//     let ms = age >= 16 & gender == 'f';

//     master &&= 'Master';
//     mr &&= 'Mr.';
//     miss &&= 'Miss';
//     ms &&= 'Ms.';
//     let persons = [master, mr, miss, ms]

//     for (let person of persons) {
//         if (person != 0) {
//             console.log(person)
//         }
//     }
// }

// personalTitles(["12", "m"])
