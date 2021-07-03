import unittest
from exercise import Subject, Student

class Test(unittest.TestCase):
    def test_subject(self):
        name = "Math"
        units = 1.5
        grade = 87.2

        s = Subject(name, units, grade)

        self.assertEqual(s.name, name)

    def test_subject_with_error_name(self):
        name = ""
        units = 1.5
        grade = 87.2 

        self.assertRaises(Exception, Subject, name, units, grade)

    def test_one_subject_gwa(self):
        name = "Math"
        units = 1.5
        grade = 87.2
        s = Subject(name, units, grade)

        name = "Patrick Starfish"
        student = Student(name)

        student.add_subject(s)

        # the weighted average should be equal to the grade
        # since we are only dealine with one subject here
        self.assertEqual(student.solve_gwa(), grade)

    ### additional laurz ###
    def test_subject_with_error_name(self):
        name = 312312
        units = 1.5
        grade = 87.2 

        self.assertRaises(Exception, Subject, name, units, grade)
    
    def test_subject_with_error_grade(self):
        name = "Math"
        units = 1.5
        grade = "87.2" 

        self.assertRaises(Exception, Subject, name, units, grade)

    def test_subject_with_error_units(self):
        name = "Math"
        units = "1.5"
        grade = 87.2 

        self.assertRaises(Exception, Subject, name, units, grade)

    def test_student_name(self):
        name = "Math"
        units = 1.5
        grade = 87.2
        s = Subject(name, units, grade)

        name = "Patrick Starfish"
        student = Student(name)

        student.add_subject(s)

        
        self.assertEqual(student.name, name)

    def test_student_name_error(self):
        name = "Math"
        units = 1.5
        grade = 87.2
        s = Subject(name, units, grade)

        name = 12.4142

        self.assertRaises(Exception, Student, name)

    def test_subjects_gwa(self):
        name = "Math"
        units = 1.5
        grade = 87.2
        s = Subject(name, units, grade)

        name = "Patrick Starfish"
        student = Student(name)

        student.add_subject(s)

        name = "Science"
        units = 3
        grade = 99.2
        s = Subject(name, units, grade)
        student.add_subject(s)

        name = "Physics"
        units = 2
        grade = 70.2
        s = Subject(name, units, grade)
        student.add_subject(s)

        # the weighted average should be equal to the grade
        # since we are only dealine with one subject here
        self.assertEqual(student.solve_gwa(), 87.50769230769232)    

if __name__ == "__main__":
    unittest.main()