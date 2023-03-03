function prepareCrystals([neededSize, ...crystals]) {
    crystals
        .forEach(size => {
            let transportingWashing = () => {
                size = Math.floor(size);
                console.log('Transporting and washing');
            }
            let operations = {
                'Cut': 0,
                'Lap': 0,
                'Grind': 0,
                'Etch': 0,
                'X-ray': 0,
                'Transporting and washing ': 0
            }

            console.log(`Processing chunk ${size} microns`);
            if (size > neededSize) {
                while (size / 4 >= neededSize) {
                    operations['Cut'] += 1;
                    size /= 4;
                }
                if (operations['Cut']) {
                    console.log(`Cut x${operations['Cut']}`);
                    transportingWashing();
                }

                if (size - size * 0.2 < size - 20) {
                    while (size - size * 0.2 >= neededSize) {
                        operations['Lap'] += 1;
                        size -= size * 0.2;
                    }
                    if (operations['Lap']) {
                        console.log(`Lap x${operations['Lap']}`)
                        transportingWashing();
                    }

                }
                while (size - 20 >= neededSize) {
                    operations['Grind'] += 1;
                    size -= 20;
                }
                if (operations['Grind']) {
                    console.log(`Grind x${operations['Grind']}`);
                    transportingWashing();
                }

                while (size - 2 >= neededSize) {
                    operations['Etch'] += 1;
                    size -= 2;
                }
                if (operations['Etch']) {
                    console.log(`Etch x${operations['Etch']}`);
                    transportingWashing();
                }

                if (size - 1 >= neededSize) {
                    operations['X-ray'] += 1;
                    size -= 1;
                    console.log(`X-ray x${operations['X-ray']}`);
                    transportingWashing();
                }

            }
            console.log(`Finished crystal ${neededSize} microns`)
        });
}

prepareCrystals([1375, 50000])