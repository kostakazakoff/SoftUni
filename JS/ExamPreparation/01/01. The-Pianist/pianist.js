function pianist(arr) {
    const numberOfPieces = Number(arr.shift());
    const piecesArr = arr.slice(0, numberOfPieces);
    const commands = arr.slice(numberOfPieces);
    const catalog = {};

    const switchCommand = {
        'Add': addPiece,
        'Remove': removePiece,
        'ChangeKey': changeKey,
    }

    function addPiece(piece, composer, key) {
        if (catalog.hasOwnProperty(piece)) {
            console.log(`${piece} is already in the collection!`);
            return;
        }
        catalog[piece] = [composer, key];
        console.log(`${piece} by ${composer} in ${key} added to the collection!`)
    }

    function removePiece(piece) {
        if (catalog.hasOwnProperty(piece)) {
            delete catalog[piece];
            console.log(`Successfully removed ${piece}!`)
            return;
        }
        console.log(`Invalid operation! ${piece} does not exist in the collection.`)
    }

    function changeKey(piece, newKey) {
        if (catalog.hasOwnProperty(piece)) {
            catalog[piece][1] = newKey;
            console.log(`Changed the key of ${piece} to ${newKey}!`)
            return;
        }
        console.log(`Invalid operation! ${piece} does not exist in the collection.`)
    }

    piecesArr.forEach(info => {
        [piece, composer, key] = info.split('|')
        catalog[piece] = [composer, key];
    })

    for (let i = 0; i < commands.length; i++) {
        [command, ...info] = commands[i].split('|');
        if (command === 'Stop') {
            Object.entries(catalog).forEach(([k, v]) => {
                console.log(`${k} -> Composer: ${v[0]}, Key: ${v[1]}`)
            })
            break;
        }
        switchCommand[command](...info);
    }
}


// pianist(
//     [
//         '3',
//         'Fur Elise|Beethoven|A Minor',
//         'Moonlight Sonata|Beethoven|C# Minor',
//         'Clair de Lune|Debussy|C# Minor',
//         'Add|Sonata No.2|Chopin|B Minor',
//         'Add|Hungarian Rhapsody No.2|Liszt|C# Minor',
//         'Add|Fur Elise|Beethoven|C# Minor',
//         'Remove|Clair de Lune',
//         'ChangeKey|Moonlight Sonata|C# Major',
//         'Stop'
//     ]
// )