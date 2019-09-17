from Adult import Adult
from Child import Child
from floridiasand import floridiasand
from compost import compost
from Person_Class import Person_Class

class Escalator_Steps:
    ''' A general container class '''

    def __init__(self, n, w, pc):
        self.nutrientReserve = n
        self.waterReserve = w
        self.Person_Class = pc