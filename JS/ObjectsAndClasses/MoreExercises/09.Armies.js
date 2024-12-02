function armies(arr) {
    let battle = {};
    let output = [];
    arr.forEach(line => {
        let leader = '';
        let action = '';
        let army = '';
        let number = 0;

        if (line.includes('arrives') || line.includes('defeated')) {
            let info = line.split(' ');
            action = info[info.length - 1];
            leader = info.splice(0, info.length - 1).join(' ');
        } else if (line.includes('+')) {
            action = '+';
            army = line.split(' + ')[0];
            number = Number(line.split(' + ')[1]);
        } else {
            [leader, info] = line.split(': ');
            army = info.split(', ')[0];
            number = Number(info.split(', ')[1]);
        }

        if (action === 'arrives') {
            if (!battle.hasOwnProperty(leader)) {
                battle[leader] = {};
            }
        } else if (action === 'defeated' && battle.hasOwnProperty(leader)) {
            delete battle[leader];
        } else if (action === '+') {
            Object.values(battle).forEach(el => {
                if (el.hasOwnProperty(army)) {
                    el[army] += number;
                }
            })
        } else if (battle.hasOwnProperty(leader)) {
            battle[leader][army] = number;
        }
    });

    let result = [];
    Object.entries(battle).forEach(([leader, leaderArmies]) => {
        if (Object.keys(leaderArmies).length !== 0) {
            let totalArmyCount = Object.values(leaderArmies).reduce((a, b) => a + b);
            let leaderArmiesUnsorted = [];

            Object.entries(leaderArmies).forEach(([k, v]) => {
                leaderArmiesUnsorted.push([k, v])
            });

            let leaderArmiesSorted = leaderArmiesUnsorted.sort((a, b) => b[1] - a[1])
            result.push([totalArmyCount, leader, leaderArmiesSorted]);
        } else {
            result.push([0, leader, []])
        }
    });

    result.sort((a, b) => b[0] - a[0]).forEach(line => {
        output.push(`${line[1]}: ${line[0]}`)
        line[2].forEach(arr => output.push(`>>> ${arr[0]} - ${arr[1]}`))
    });

    console.log(output.join('\n'))
}


// armies(
//     [
//         'Rick Burr arrives',
//         'Findlay arrives',
//         'Rick Burr: Juard, 1500',
//         'Wexamp arrives',
//         'Findlay: Wexamp, 34540',
//         'Wexamp + 340',
//         'Wexamp: Britox, 1155',
//         'Wexamp: Juard, 43423',
//         'Wexamp arrives'
//     ]
// )
