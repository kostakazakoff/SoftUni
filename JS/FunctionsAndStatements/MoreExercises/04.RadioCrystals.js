function prepareCrystals([neededSize, ...crystals]) {
    crystals
        .forEach(size => {
            let transportingWashing = () => {
                size = Math.floor(size);
                console.log('Transporting and washing');
            }
                let cut = 0;
                let lap = 0;
                let grind = 0;
                let etch = 0;

            console.log(`Processing chunk ${size} microns`);
            if (size > neededSize) {
                while (size / 4 >= neededSize) {
                    cut += 1;
                    size /= 4;
                }
                if (cut) {
                    console.log(`Cut x${cut}`);
                    transportingWashing();
                }

                if (size - size * 0.2 < size - 20) {
                    while (size - size * 0.2 >= neededSize - 1) {
                        lap += 1;
                        size -= size * 0.2;
                    }
                    if (lap) {
                        console.log(`Lap x${lap}`)
                        transportingWashing();
                    }

                }
                while (size - 20 >= neededSize -1) {
                    grind += 1;
                    size -= 20;
                }
                if (grind) {
                    console.log(`Grind x${grind}`);
                    transportingWashing();
                }

                while (size - 2 >= neededSize - 1) {
                    etch += 1;
                    size -= 2;
                }
                if (etch) {
                    console.log(`Etch x${etch}`);
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