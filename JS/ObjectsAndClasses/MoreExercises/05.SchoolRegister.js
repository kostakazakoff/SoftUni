function schoolRegister(arr) {
    let nextGrade = {};
    output = [];
    
    arr.map(studend => studend.split(', ')
        .map(studentInfo => studentInfo.split(': ')[1]))
        .forEach(student => {
            if (!nextGrade[student[1]]) {
                nextGrade[student[1]] = {};
            }

            if (Number(student[2]) >= 3) {
                nextGrade[student[1]][student[0]] = Number(student[2]);
            }
        });

    Object.entries(nextGrade).forEach(([grade, students]) => {
        if (Object.keys(students).length !== 0) {
            output.push(`${Number(grade) + 1} Grade`);
            let studentsInClass = [];
            let scores = [];

            for (let student in students) {
                studentsInClass.push(student);
                scores.push(students[student]);
            }

            classAverageScore = (scores.reduce((a, b) => a + b) / scores.length).toFixed(2);
            output.push(`List of students: ${studentsInClass.join(', ')}`);
            output.push(`Average annual score from last year: ${classAverageScore}`);
            output.push(``);
        }
    })
    console.log(output.join('\n'))
}

schoolRegister([
    'Student name: George, Grade: 5, Graduated with an average score: 2.75',
    'Student name: Alex, Grade: 9, Graduated with an average score: 3.66',
    'Student name: Peter, Grade: 8, Graduated with an average score: 2.83',
    'Student name: Boby, Grade: 5, Graduated with an average score: 4.20',
    'Student name: John, Grade: 9, Graduated with an average score: 2.90',
    'Student name: Steven, Grade: 2, Graduated with an average score: 4.90',
    'Student name: Darsy, Grade: 1, Graduated with an average score: 5.15'
]
)