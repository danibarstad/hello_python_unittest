'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    ## TODO write a test that adds and removes a student, and asserts the student is removed. Use assertNotIn
    def test_add_remove_student(self):
        test_class = ClassList(1)
        test_class.add_student('Spongebob')
        test_class.remove_student('Spongebob')

        self.assertNotIn('Spongebob', test_class.class_list)


    ## TODO write a test that adds some example students, then removes a student not in the list, and asserts a StudentError is raised
    def test_remove_student_not_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Mega Man')
        test_class.add_student('Proto Man')
        test_class.add_student('Flash Man')

        with self.assertRaises(StudentError):
            test_class.remove_student('Dani Man')


    ## TODO write a test that removes a student from an empty list, and asserts a StudentError is raised
    def test_remove_from_empty_list(self):
        test_class = ClassList(0)

        with self.assertRaises(StudentError):
            test_class.remove_student('Pennywise')


    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    ## TODO write a test that adds some example students to a test class,
    ## then, call is_enrolled for a student who is not enrolled. use assertFalse to verify is_enrolled returns false.
    def test_student_not_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Rodrigo')
        test_class.add_student('Gabriela')

        self.assertFalse(test_class.is_enrolled('Dani'))


    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


    ## However, it would be useful to check that index_of_student returns None if a student isn't present.
    ## TODO write a test for index_of_student to assert it returns None if the student is not in the list if the list is empty. use assertIsNone.
    ## TODO write another test when the list is not empty but does not contain the student name, assert that the correct index is returned.
    def test_index_of_student_not_present(self):
        test_class = ClassList(0)

        self.assertIsNone(test_class.index_of_student(''))
    
    def test_index_of_student_empty_list(self):
        test_class = ClassList(2)
        test_class.add_student('Rick')
        test_class.add_student('Morty')

        self.assertIsNone(test_class.index_of_student(''))


    ## TODO write a test for your new is_class_full method when the class is full. use assertTrue
    ## TODO write a test for your new is_class_full method for when is empty, and when it is not full. Use assertFalse
    def test_is_class_full(self):
        test_list = ClassList(4)
        test_list.add_student('James Hetfield')
        test_list.add_student('Lars Ulrich')
        test_list.add_student('Kirk Hammett')
        test_list.add_student('Rob Trujillo')

        self.assertTrue(test_list.is_class_full())
    
    def test_is_class_empty(self):
        test_list = ClassList(4)
        test_list.add_student('James Hetfield')
        test_list.add_student('Lars Ulrich')
        test_list.add_student('Kirk Hammett')
        
        self.assertFalse(test_list.is_class_full())