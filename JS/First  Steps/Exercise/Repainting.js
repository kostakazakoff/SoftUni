function calcRepainting(params) {
    let nylonNeeded = Number(params[0]) + 2;
    let paintNeeded = Number(params[1]) * 1.1;
    let thinnerNeeded = Number(params[2]);
    let workingHours = Number(params[3]);
    let bags = 0.4;
    let materialsTotal = nylonNeeded * 1.5 + paintNeeded * 14.5 + thinnerNeeded * 5 + bags;
    let pricePerHour = materialsTotal * 0.3;
    let workPriceTotal = workingHours * pricePerHour;
    let totalExpences = materialsTotal + workPriceTotal;
    console.log(totalExpences);
}