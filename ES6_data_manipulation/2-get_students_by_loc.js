// function that return an array of objects located in a specific city

export default function getStudentsByLocation(students, city) {
  const studentbylocation = students.filter((student) => student.location === city);
  return studentbylocation;
}
