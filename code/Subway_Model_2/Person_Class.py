class Person_Class:
    ''' A class for people riding the subway'''

    def __init__(self, l, r):
        '''Intializes the Person_Class'''
        self.length = l
        self.radius = r


    def __str__(self):
        '''Definition for the print statement'''
        return "Person_Class: '{}' of type ({}) weighs {} grams.".format(
            self.name,str(self.__class__.__name__),
            str(self.length))

