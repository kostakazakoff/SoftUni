function calcStoreProvision(current, ordered) {
    let provision = {};

    function parseToObj(arr) {
        for (let i = 0; i < arr.length; i+=2) {
            if (!provision.hasOwnProperty(arr[i])) {
                provision[arr[i]] = 0;
            };
            provision[arr[i]] += parseInt(arr[i+1]);
        };
    };

    parseToObj([...current, ...ordered]);

    for (key in provision) {
        console.log(`${key} -> ${provision[key]}`);
    };
}

calcStoreProvision([
    'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
    ],
    [
    'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ]
    )