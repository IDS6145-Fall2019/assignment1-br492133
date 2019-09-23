import math
from Escalator_Step import Escalator_Step

class Escalator:
    '''An ASME-standard compliant escalator step'''

    def __init__(self, l, w):
        '''Intializes the Escalator Step'''
        self.length = 44
        self.width = 8.5 * Escalator_Step