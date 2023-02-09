function figureAreaCalc(params) {
    let figure = params[0];
    if (figure === "square") {
        let area = (Number(params[1]) ** 2).toFixed(3);
        console.log(area);
    } else if (figure === "rectangle") {
        let area = (Number(params[1]) * Number(params[2])).toFixed(3);
        console.log(area);
    } else if (figure === "circle") {
        let area = (Math.PI * Number(params[1]) ** 2).toFixed(3);
        console.log(area);
    } else if (figure === "triangle") {
        let area = (Number(params[1]) * Number(params[2]) / 2).toFixed(3);
        console.log(area);
    }
}