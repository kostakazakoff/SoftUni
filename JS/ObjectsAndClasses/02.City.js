function loopTheObj(obj) {
    for (key in obj) {
        console.log(`${key} -> ${obj[key]}`)
    }
}