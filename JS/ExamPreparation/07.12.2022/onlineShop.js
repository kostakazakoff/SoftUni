class OnlineShop {
    constructor(warehouseSpace) {
        this.warehouseSpace = warehouseSpace;
        this.products = [];
        this.sales = [];
    }

    loadingStore(product, quantity, spaceRequired) {
        if (this.warehouseSpace < spaceRequired) {
            throw new Error('Not enough space in the warehouse.')
        }
        this.products.push({ product, quantity });
        this.warehouseSpace -= spaceRequired;
        return `The ${product} has been successfully delivered in the warehouse.`
    }

    quantityCheck(product, minimalQuantity) {
        if (minimalQuantity <= 0) {
            throw new Error('The quantity cannot be zero or negative.')
        }
        for (const p of this.products) {
            if (p.product === product && p.quantity >= minimalQuantity) {
                return `You have enough from product ${product}.`
            } else if (p.product === product && p.quantity) {
                const difference = minimalQuantity - p.quantity;
                p.quantity = minimalQuantity;
                return `You added ${difference} more from the ${product} products.`;
            }
        }
        throw new Error(`There is no ${product} in the warehouse.`);
    }

    sellProduct(productToSale) {
        for (const p of this.products) {
            if (p.product === productToSale) {
                p.quantity--;
                const quantity = 1;
                const product = productToSale;
                this.sales.push({ product, quantity });
                return `The ${productToSale} has been successfully sold.`;
            }
        }
        throw new Error(`There is no ${productToSale} in the warehouse.`)
    }

    revision() {
        if (this.sales.length === 0) {
            throw new Error(`There are no sales today!`);
        }
        let output = [`You sold ${this.sales.length} products today!`, 'Products in the warehouse:'];
        for (const p of this.products) {
            output.push(`${p.product}-${p.quantity} more left`)
        }
        return output.join('\n')
    }
}


// const myOnlineShop = new OnlineShop(500)
// console.log(myOnlineShop.loadingStore('headphones', 10, 200));
// console.log(myOnlineShop.loadingStore('laptop', 5, 200));

// console.log(myOnlineShop.quantityCheck('headphones', 10));
// console.log(myOnlineShop.quantityCheck('laptop', 10));

// console.log(myOnlineShop.sellProduct('headphones'));
// console.log(myOnlineShop.sellProduct('laptop'));
// console.log(myOnlineShop.revision());