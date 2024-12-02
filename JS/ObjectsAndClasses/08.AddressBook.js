function addressBook(arr) {
    let addressBookObject = {};
    arr.forEach(person => {
        [pName, pAddress] = person.split(':');
        addressBookObject[pName] = pAddress;
    });
    Object.keys(addressBookObject)
    .sort((a, b) => a.localeCompare(b))
    .forEach(person => console.log(`${person} -> ${addressBookObject[person]}`));
}

// addressBook(['Tim:Doe Crossing',
// 'Bill:Nelson Place',
// 'Peter:Carlyle Ave',
// 'Bill:Ornery Rd']
// )