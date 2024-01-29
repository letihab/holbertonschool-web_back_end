// function that returns an array of ids

export default function getListStudentIds(studentsArray) {
  if (!Array.isArray(studentsArray)) {
    return [];
  }

  const studentIds = studentsArray.map((student) => student.id);
  return studentIds;
}
