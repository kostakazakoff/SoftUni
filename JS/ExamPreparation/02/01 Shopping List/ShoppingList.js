function solve(arr) {
    let productsList = arr.shift().split('!');
    const endIdx = arr.indexOf('Go Shopping!');
    const allCommands = arr.slice(0, endIdx);
    const execute = {
        'Urgent': addItemAtStart,
        'Unnecessary': removeItem,
        'Correct': renameItem,
        'Rearrange': moveItemAtEnd
    }

    allCommands.forEach(commandLine => {
        const [command, ...items] = commandLine.split(' ');
        execute[command](items);
    });

    function addItemAtStart(products) {
        const [product] = products
        if (productsList.includes(product)) { return };
        productsList.unshift(product);
    }

    function removeItem(products) {
        const [product] = products
        if (!productsList.includes(product)) { return };
        const idx = productsList.indexOf(product);
        productsList.splice(idx, 1);
    }

    function renameItem(products) {
        const [oldName, newName] = products;
        if (!productsList.includes(oldName)) { return };
        const idx = productsList.indexOf(oldName);
        productsList[idx] = newName;
    }

    function moveItemAtEnd(products) {
        const [product] = products
        if (!productsList.includes(product)) { return };
        const idx = productsList.indexOf(product);
        productsList.splice(idx, 1);
        productsList.push(product);
    }

    console.log(productsList.join(', '));
}

solve(
    (["Milk!Pepper!Salt!Water!Banana",
        "Urgent Salt",
        "Unnecessary Grapes",
        "Correct Pepper Onion",
        "Rearrange Grapes",
        "Correct Tomatoes Potatoes",
        "Go Shopping!"])
)