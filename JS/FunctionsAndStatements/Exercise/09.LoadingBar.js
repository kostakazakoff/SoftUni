function loadingBar(number) {
    const loaded = number / 10;
    const unloaded = 10 - loaded;
    let loadedBars = '%'.repeat(loaded);
    let unloadedBars = '.'.repeat(unloaded);
    if (unloaded) {
        console.log(`${number}% [${loadedBars}${unloadedBars}]`);
        console.log('Still loading...');
    } else {
        console.log(`${number}% Complete!`);
        console.log(`[${loadedBars}${unloadedBars}]`);
    }
}

// loadingBar(100)