function convertToJson(name, lastName, hairColor) {
    person = {name, lastName, hairColor};
    jsonString = JSON.stringify(person);
    console.log(jsonString);
}