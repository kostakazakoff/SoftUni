function employeePersonalNumber(arr) {
    let book = {};
    arr.forEach(employee => {
        book[employee] = employee.length;
    });
    for (person in book) {
        console.log(`Name: ${person} -- Personal Number: ${book[person]}`);
    }
}

// employeePersonalNumber([
//     'Silas Butler',
//     'Adnaan Buckley',
//     'Juan Peterson',
//     'Brendan Villarreal'
//     ]
//     )