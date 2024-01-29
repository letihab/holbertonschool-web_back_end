// function that returns the sum of all the students ids

export default function getStudentIdsSum(students) {
  const studentIds = students.map((student) => student.id);
  const sum = studentIds.reduce((total, studentId) => total + studentId + 0);
  return sum;
}
