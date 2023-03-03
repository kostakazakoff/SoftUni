function carWash(commands) {
    let cleaned = 0;
    let soap = () => cleaned += 10;
    let water = () => cleaned *= 1.2;
    let vacuumCleaner = () => cleaned *= 1.25;
    let mud = () => cleaned *= 0.9;

    const actions = {
        'soap': soap,
        'water': water,
        'vacuum cleaner': vacuumCleaner,
        'mud': mud
    }

    commands.forEach(command => {
        actions[command]();
    });

    console.log(`The car is ${cleaned.toFixed(2)}% clean.`)
}

// carWash(['soap', 'soap', 'vacuum cleaner', 'mud', 'soap', 'water'])