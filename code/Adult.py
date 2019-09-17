import math
from Person_Class import Person_Class

class Adult(Person_Class):
    '''This is a string bean'''

    def __init__(self, n, w, wet, c):
        '''Set the name and vertices of the shape'''
        soil.__init__(self,n, w, wet, c)


    def ProvideNutrients(self):
        '''Every vegtable grows differently'''
        if self.nutrients >= 10.0:
            self.nutrients -= 10.0
            return 10.0
        else:
            return None