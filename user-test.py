import unittest
from user import user

class Testuser(unittest.TestCase):
    
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = user("Evan","kimani","2021") # create contact object
def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Evan")
        
       
        self.assertEqual(self.new_user.password,"2021")            