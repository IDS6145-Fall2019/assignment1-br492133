import math
from Person_Class import Person_Class

class Child(Person_Class):
    '''This is a Child'''

    def __init__(self, name):
        '''Intializes the Child-sized person class'''
        self.name = Child
        self.length =  36
        self.radius = 4
        Person_Class.__init__(self, name, self.length, self.radius)
