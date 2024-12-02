function convertToObject(jsonString) {
    let obj = JSON.parse(jsonString);
    for (key in obj) {
        console.log(`${key}: ${obj[key]}`);
    };
}

// convertToObject('{"name": "George", "age": 40, "town": "Sofia"}')