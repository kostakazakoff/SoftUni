function prepareCrystals([neededSize, ...crystals]) {
    crystals
        .forEach(size => {
            const transportingWashing = () => {
                size = Math.floor(size);
                console.log('Transporting and washing');
            }
            let cutCounter = 0;
            let lapCounter = 0;
            let grindCounter = 0;
            let etchCounter = 0;

            console.log(`Processing chunk ${size} microns`);
            if (size > neededSize) {
                while (size / 4 >= neededSize) {
                    cutCounter += 1;
                    size /= 4;
                }
                if (cutCounter) {
                    console.log(`Cut x${cutCounter}`);
                    transportingWashing();
                }

                if (size - size * 0.2 < size - 20) {
                    while (size - size * 0.2 >= neededSize - 1) {
                        lapCounter += 1;
                        size -= size * 0.2;
                    }
                    if (lapCounter) {
                        console.log(`Lap x${lapCounter}`)
                        transportingWashing();
                    }

                }
                while (size - 20 >= neededSize - 1) {
                    grindCounter += 1;
                    size -= 20;
                }
                if (grindCounter) {
                    console.log(`Grind x${grindCounter}`);
                    transportingWashing();
                }

                while (size - 2 >= neededSize - 1) {
                    etchCounter += 1;
                    size -= 2;
                }
                if (etchCounter) {
                    console.log(`Etch x${etchCounter}`);
                    transportingWashing();
                }

                if (size < neededSize) {
                    size += 1;
                    console.log(`X-ray x1`);
                }

            }
            console.log(`Finished crystal ${neededSize} microns`)
        });
}

prepareCrystals([1375, 50000])