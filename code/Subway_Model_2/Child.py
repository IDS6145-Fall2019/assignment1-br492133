import math
from Person_Class import Person_Class

class pepper(Person_Class):
    '''This is a Child'''

    def __init__(self, l, r):
        '''Intializes the Child-sized person class'''
        self.length =  36
        self.radius = 4
        Person_Class.__init__(self, l, r)
