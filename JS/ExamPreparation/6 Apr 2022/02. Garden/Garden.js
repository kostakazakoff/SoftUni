class Garden {
    constructor(spaceAvailable) {
        this.spaceAvailable = spaceAvailable;
        this.plants = [];
        this.storage = [];
    }

    addPlant(plantName, spaceRequired) {
        if (spaceRequired > this.spaceAvailable) {
            throw new Error('Not enough space in the garden.');
        }
        this.plants.push({ plantName, spaceRequired, ripe: false, quantity: 0 });
        this.spaceAvailable -= spaceRequired;
        return `The ${plantName} has been successfully planted in the garden.`
    }

    ripenPlant(plantName, quantity) {
        if (quantity <= 0) {
            throw new Error('The quantity cannot be zero or negative.');
        }
        const plant = this.plants.find(p => p.plantName === plantName);
        if (!plant) {
            throw new Error(`There is no ${plantName} in the garden.`);
        }
        if (plant.ripe) {
            throw new Error(`The ${plantName} is already ripe.`)
        }
        const idx = this.plants.indexOf(plant);
        this.plants[idx].quantity += quantity;
        this.plants[idx].ripe = true;
        if (quantity === 1) {
            return `${quantity} ${plantName} has successfully ripened.`;
        }
        return `${quantity} ${plantName}s have successfully ripened.`
    }

    harvestPlant(plantName) {
        const plant = this.plants.find(p => p.plantName === plantName);
        if (!plant) {
            throw new Error(`There is no ${plantName} in the garden.`);
        }
        if (!plant.ripe) {
            throw new Error(`The ${plantName} cannot be harvested before it is ripe.`);
        }
        const quantity = plant.quantity;
        this.storage.push({ plantName, quantity });
        this.spaceAvailable += quantity;
        const idx = this.plants.indexOf(plant);
        this.plants.splice(idx, 1);
        return `The ${plantName} has been successfully harvested.`
    }

    generateReport() {
        let output = [`The garden has ${this.spaceAvailable} free space left.`];
        let plantsList = ['Plants in the garden: '];

        const sorted = this.plants.map(p => p.plantName).sort((a, b) => a.localeCompare(b));
        sorted.forEach(plant => plantsList.push(plant));

        plantsList = plantsList.join(', ');
        output.push(plantsList);

        let plantsInStorage = ['Plants in storage: '];

        if (this.storage.length === 0) {
            plantsInStorage.push('The storage is empty.')
        } else {
            this.storage.forEach(p => plantsInStorage.push(`${p.plantName} (${p.quantity})`));
            plantsInStorage = plantsInStorage.join(', ');
        }

        output.push(plantsInStorage);
        return output.join('\n');
    }
}


// const myGarden = new Garden(250)
// console.log(myGarden.addPlant("apple", 20));
// console.log(myGarden.addPlant("orange", 200));
// console.log(myGarden.ripenPlant("orange", 1));
// console.log(myGarden.harvestPlant("orange"));
// console.log(myGarden.generateReport());



//Testing generateReport
// const Garden = result;
// let myGarden = new Garden(250);

// assert.equal(myGarden.addPlant("apple", 20), "The apple has been successfully planted in the garden.");
// assert.equal(myGarden.addPlant("orange", 200), "The orange has been successfully planted in the garden.");
// assert.equal(myGarden.addPlant("raspberry", 10), "The raspberry has been successfully planted in the garden.");
// assert.equal(myGarden.ripenPlant("apple", 10), "10 apples have successfully ripened.");
// assert.equal(myGarden.ripenPlant("orange", 1), "1 orange has successfully ripened.");
// assert.equal(myGarden.harvestPlant("orange"), "The orange has been successfully harvested.");
// assert.equal(myGarden.generateReport(), "The garden has 220 free space left.\nPlants in the garden: apple, raspberry\nPlants in storage: orange (1)");
