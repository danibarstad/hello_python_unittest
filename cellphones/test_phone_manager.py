import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        # TODO add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        # TODO you'll need to modify PhoneAssignments.add_phone() to make this test pass
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)


    def test_create_and_add_new_employee(self):
        # TODO write this test and then remove the self.fail() statement
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        testEmployee1 = Employee(1, 'James')
        testEmployee2 = Employee(2, 'Dani')

        testEmployees = [ testEmployee1, testEmployee2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_employee(testEmployee2)

        self.assertCountEqual(testEmployees, testAssignmentMgr.employees)
        # self.fail()


    def test_create_and_add_employee_with_duplicate_id(self):
        # TODO write this test and then remove the self.fail() statement
        # TODO you'll need to fix the add_employee method in PhoneAssignments to make this test PhoneAssignments
        # This method will be similar to test_create_and_add_phone_with_duplicate_id
        testEmployee1 = Employee(1, 'Noel')
        testEmployee2 = Employee(1, 'Liam')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(testEmployee2)
        # self.fail()


    def test_assign_phone_to_employee(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments

        testEmployee = Employee(1, 'Lemmy')
        testPhone = Phone(1, 'Motorola', 'G4 Play')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee)
        testAssignmentMgr.add_phone(testPhone)
        testAssignmentMgr.assign(testPhone.id, testEmployee)

        self.assertTrue(testPhone.is_assigned, True)
        # self.fail()


    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it throws an exception if the phone is alreaady assigned.

        testEmployee = Employee(1, 'Milli')
        testEmployee2 = Employee(2, 'Vanilli')
        testPhone = Phone(1, 'Apple', 'iPhone ∞')

        testAssignmentMgr = PhoneAssignments()

        testAssignmentMgr.add_employee(testEmployee)
        testAssignmentMgr.add_employee(testEmployee2)
        testAssignmentMgr.add_phone(testPhone)
        
        testAssignmentMgr.assign(testPhone.id, testEmployee)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone.id, testEmployee2)
        # self.fail()


    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.

        testEmployee = Employee(1, 'MC Bat Commander')
        testPhone = Phone(1, 'Apple', 'iPhone')
        testPhone2 = Phone(2, 'Dumb Apple', 'Dumb iPhone')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.assign(testPhone.id, testEmployee)
        
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone2.id, testEmployee)
        # self.fail()


    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.

        testEmployee = Employee(1, 'Danzig')
        testPhone = Phone(1, 'Metalocalypse', 'Dethphone')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.assign(testPhone.id, testEmployee)


        # self.fail()


    def test_un_assign_phone(self):
        # TODO write this test and remove the self.fail() statement
        # Assign a phone, unassign the phone, verify the employee_id is None
        testEmployee = Employee(1, 'Andre the Giant')
        testPhone = Phone(1, 'Google', 'Pixel 3a')

        testAssignmentMgr = PhoneAssignments()

        testAssignmentMgr.assign(testPhone.id, testEmployee)
        testAssignmentMgr.un_assign(testPhone.id)

        self.assertIsNone(testAssignmentMgr.phone_info(testEmployee))
        # self.fail()


    def test_get_phone_info_for_employee(self):
        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # TODO check that the method returns None if the employee does not have a phone
        # TODO check that the method raises an PhoneError if the employee does not exist
        testEmployee1 = Employee(1, 'Dani')
        testEmployee2 = Employee(2, 'Beryl')
        testEmployee3 = Employee(3, 'Archie')
        testEmployee4 = None

        testPhone1 = Phone(1, 'Apple', 'New iPhone 10 Pro XL lite++ Max')
        testPhone2 = Phone(2, 'Nintendo', 'Nintendo Switch Cell Phone')

        testAssignmentMgr = PhoneAssignments()

        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_employee(testEmployee2)
        testAssignmentMgr.add_employee(testEmployee3)
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.assign(testPhone1.id, testEmployee1)
        testAssignmentMgr.assign(testPhone2.id, testEmployee2)

        # self.assertEqual('ID: 1 Make: Apple Model: New iPhone 10 Pro XL lite++ Max Assigned to Employee ID: 1', testAssignmentMgr.phone_info(testEmployee1))
        # self.assertEqual('ID: 2 Make: Nintendo Model: Nintendo Switch Cell Phone Assigned to Employee ID: 2', testAssignmentMgr.phone_info(testEmployee2))

        with self.assertRaises(PhoneError):
            testAssignmentMgr.phone_info(testEmployee4)

        # self.fail()
