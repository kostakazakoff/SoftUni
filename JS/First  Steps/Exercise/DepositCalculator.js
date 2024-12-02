function calcInterest(params) {
    let deposit = Number(params[0]);
    let term = Number(params[1]);
    let annualInterestRate = Number(params[2]) / 100;
    let interest = deposit + term * ((deposit * annualInterestRate) / 12)
    console.log(interest)
}