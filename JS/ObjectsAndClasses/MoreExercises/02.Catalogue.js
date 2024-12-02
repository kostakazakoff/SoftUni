function orderCatalogue(arr) {
    let headers = new Set();

    let articles = Object.entries(
        arr.reduce((data, article) => {
            headers.add(article[0].toUpperCase());
            let art = article.split(' : ');
            data[art[0]] = art[1];
            return data;
        }, {})
    ).sort((a, b) => (a[0].toLowerCase()).localeCompare(b[0].toLowerCase()))
    
    headers = Array.from(headers).sort();

    for (h of headers) {
        console.log(h)
        for (a of articles) {
            if (a[0][0] == h) {
                console.log(`  ${a[0]}: ${a[1]}`);
            }
        }
    }
}


// orderCatalogue(
//     [
//         'Appricot : 20.4',
//         'Fridge : 1500',
//         'TV : 1499',
//         'Deodorant : 10',
//         'Boiler : 300',
//         'Apple : 1.25',
//         'Anti-Bug Spray : 15',
//         'T-Shirt : 10'
//     ]

// )