function Inventory(arr) {
    let heroes = [];
    arr.forEach(line => {
        let [heroName, level, items] = line.split(' / ');
        let hero = { heroName, level, items };
        heroes.push(hero);
    });

    heroes
    .sort((heroA, heroB) => heroA.level - heroB.level)
    .forEach(hero => {
        console.log(`Hero: ${hero.heroName}`);
        console.log(`level => ${hero.level}`);
        console.log(`items => ${hero.items}`);
    })
}

Inventory([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
]
)
