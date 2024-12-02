function formatGrade(grade) {
    let description;
    if (grade < 3) {
        description = `Fail (2)`;
    } else if (grade < 3.5) {
        description = `Poor (${grade.toFixed(2)})`;
    } else if (grade < 4.5) {
        description = `Good (${grade.toFixed(2)})`;
    } else if (grade < 5.5) {
        description = `Very good (${grade.toFixed(2)})`;
    } else {
        description = `Excellent (${grade.toFixed(2)})`;
    }
    console.log(description)
}