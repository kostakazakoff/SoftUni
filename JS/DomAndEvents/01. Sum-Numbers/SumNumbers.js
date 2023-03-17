function calc() {
    const inputs = Array.from(document.getElementsByTagName('input'));
    const resultField = inputs[2];
    let nums = inputs.slice(0, 2).map(n => Number(n.value));
    resultField.value = nums.reduce((n1, n2) => n1 + n2);
}