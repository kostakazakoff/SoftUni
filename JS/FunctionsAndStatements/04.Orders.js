function calcOrder(product, quantity) {
    let price;
    switch (product) {
        case 'coffee':
            price = 1.5;
            break;
        case 'water':
            price = 1;
            break;
        case 'coke':
            price = 1.4;
            break;
        case 'snacks':
            price = 2;
    }
    let result = price * quantity;
    console.log((price * quantity).toFixed(2))
}

calcOrder("coffee", 2)