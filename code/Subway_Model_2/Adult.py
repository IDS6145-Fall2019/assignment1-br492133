import math
from Person_Class import Person_Class

class eggplant(Person_Class):
    '''This is an adult escalator rider'''

    def __init__(self, l, r):
        '''Intializes the Adult sized person class'''
        self.length = 72
        self.radius = 6
        Person_Class.__init__(self, l, r)
