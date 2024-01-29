// function that return an array of etudents for a specific city with their new grade

export default function updateStudentGradeByCity(students, city, newGrades) {
    const filterstudents = students.filter((student) => student.location === city);

}