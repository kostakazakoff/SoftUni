class WineSelection {
    constructor(space) {
        this.space = space;
        this.wines = [];
        this.bill = 0;
    }

    reserveABottle(wineName, wineType, price) {
        if (this.space) {
            this.space--;
            this.wines.push({ wineName, wineType, price, 'paid': false });
            return `You reserved a bottle of ${wineName} ${wineType} wine.`;
        }
        throw new Error('Not enough space in the cellar.');
    }

    payWineBottle(wineName, price) {
        for (const wine of this.wines) {
            if (wineName === wine.wineName && !wine.paid) {
                wine.paid = true;
                this.bill += price;
                return `You bought a ${wineName} for a ${price}$.`;
            }
        }
        throw new Error(`${wineName} is not in the cellar.`)
    }

    openBottle(wineName) {
        for (const wine of this.wines) {
            if (wineName === wine.wineName && wine.paid) {
                const idx = this.wines.indexOf(wine);
                this.wines.splice(idx, 1);
                return `You drank a bottle of ${wineName}.`
            } else if (wineName === wine.wineName && !wine.paid) {
                throw new Error(`${wineName} need to be paid before open the bottle.`)
            }
        }
        throw new Error("The wine, you're looking for, is not found.")
    }

    cellarRevision(wineType) {
        let output = [];
        if (wineType === undefined) {
            output.push(`You have space for ${this.space} bottles more.`);
            output.push(`You paid ${this.bill}$ for the wine.`);
            this.wines.sort((a, b) => a.wineName.localeCompare(b.wineName))
                .forEach(w => {
                    let paidInfo = this.winePaidInfo(w);
                    output.push(`${w.wineName} > ${w.wineType} - ${paidInfo}.`);
                });
            return output.join('\n')
        } else if (wineType !== undefined) {
            for (const w of this.wines) {
                if (w.wineType === wineType) {
                    let paidInfo = this.winePaidInfo(w);
                    output.push(`${w.wineName} > ${w.wineType} - ${paidInfo}.`)
                }
            }
            if (output.length > 0) { return output.join('\n') };
        }
        throw new Error(`There is no ${wineType} in the cellar.`)
    }

    winePaidInfo(wine) {
        let paidInfo;
        if (wine.paid) { paidInfo = 'Has Paid' } else { paidInfo = 'Not Paid' };
        return paidInfo;
    }
}

const selection = new WineSelection(5)
selection.reserveABottle('Bodegas Godelia Mencía', 'Rose', 144);
selection.payWineBottle('Bodegas Godelia Mencía', 144);
selection.reserveABottle('Sauvignon Blanc Marlborough', 'White', 50);
selection.reserveABottle('Cabernet Sauvignon Napa Valley', 'Red', 120);
console.log(selection.cellarRevision());
