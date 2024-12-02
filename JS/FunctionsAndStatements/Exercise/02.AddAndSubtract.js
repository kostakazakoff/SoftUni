function addAndSubtract(a, b, c) {
    const add = (n1, n2) => n1 + n2;
    const subtract = (n1, n2) => n1 - n2;
    console.log(subtract(add(a, b), c));
}

addAndSubtract(23,
    6,
    10
    )