function calcSuppliesPrice(params) {
    let pencils = Number(params[0]) * 5.8;
    let markers = Number(params[1]) * 7.2;
    let abstergent = Number(params[2]) * 1.2;
    let discount = Number(params[3]) / 100;
    let total = (pencils + markers + abstergent);
    let result = total * (1 - discount);
    console.log(result);
}