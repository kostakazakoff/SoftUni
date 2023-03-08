function addContacts(arrOfContacts) {
    let contacts = {};
    arrOfContacts.forEach(contact => {
        [contactName, phone] = contact.split(' ');
        contacts[contactName] = phone;
    });
    for (key in contacts) {
        console.log(`${key} -> ${contacts[key]}`);
    };
}