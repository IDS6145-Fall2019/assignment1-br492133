import math
class Person_Class:
    ''' A class for people riding the subway'''

    def __init__(self, name, l, r):
        '''Intializes the Person_Class'''
        self.name = name
        self.length = l
        self.radius = r

    def Person_Name(self):
        print('I am a subway rider -', self.name)

