from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Student1", None)
        self.student_with_courses = Student("Student2", {'Python': ['a', 'b']})

    def test__initialising(self):
        self.assertEqual("Student1", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Student2", self.student_with_courses.name)
        self.assertEqual({'Python': ['a', 'b']}, self.student_with_courses.courses)

    def test__enroll__course_exist(self):
        result = self.student_with_courses.enroll('Python', ['c', 'd'], '')
        self.assertEqual({'Python': ['a', 'b', 'c', 'd']}, self.student_with_courses.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test__enroll__course_not_exist_not_confirmed_add_notes(self):
        result = self.student.enroll('Python', ['c', 'd'], 'N')
        self.assertEqual({'Python': []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test__enroll__course_not_exist_confirmed_add_notes(self):
        result = self.student.enroll('Python', ['c', 'd'], '')
        self.assertEqual({'Python': ['c', 'd']}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test__enroll__course_not_exist_confirmed_add_notes_y(self):
        result = self.student.enroll('Python', ['c', 'd'], 'Y')
        self.assertEqual({'Python': ['c', 'd']}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test__add_notes__course_exist(self):
        result = self.student_with_courses.add_notes('Python', 'c')
        self.assertEqual({'Python': ['a', 'b', 'c']}, self.student_with_courses.courses)
        self.assertEqual("Notes have been updated", result)

    def test__add_notes__course_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Python', 'c')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual({}, self.student.courses)

    def test__leave_course_exist(self):
        result = self.student_with_courses.leave_course('Python')
        self.assertEqual({}, self.student_with_courses.courses)
        self.assertEqual("Course has been removed", result)

    def test__leave_course_not_exist(self):
        with self.assertRaises(Exception) as ex:
            result = self.student.leave_course('Python')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
