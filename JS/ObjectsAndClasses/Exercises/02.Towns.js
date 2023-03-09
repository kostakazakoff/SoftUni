function townsLocation(arr) {
    let townsCatalog = [];

    function parseElement(array) {
        let [town, ...position] = array.split(' | ');
        [latitude, longitude] = position.map(x => parseFloat(x).toFixed(2));
        return [town, latitude, longitude];
    }

    arr.forEach(element => {
        let [town, latitude, longitude] = parseElement(element);
        townsCatalog.push({town, latitude, longitude});
    });

    townsCatalog.forEach(el => {
        console.log(el);
    });
}

// townsLocation(['Sofia | 42.696552 | 23.32601',
// 'Beijing | 39.913818 | 116.363625']
// )