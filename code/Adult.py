import math
from Person_Class import Person_Class

class Adult(Person_Class):
    '''This is an adult escalator rider'''

    def __init__(self, name):
        '''Intializes the Adult sized person class'''
        self.name = Adult
        self.length =  72
        self.radius = 6
        Person_Class.__init__(self, name, self.length, self.radius)

    def Person_A(self):
        print('I am an ', self.name)