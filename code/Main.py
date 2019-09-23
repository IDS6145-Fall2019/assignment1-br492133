import math, time, _thread, sys, os
from Person_Class import Person_Class
from Adult import Adult
from Child import Child
from Escalator_Step import Escalator_Step
from Escalator import Escalator


# Remember this method gets executed first since it's our 'main'
def main():
    #Make some people and steps
    Make_People_C = Child('Child')
    Make_People_C.Person_Name()

    Make_People_A= Adult('Adult')
    Make_People_A.Person_Name()

if __name__ == "__main__":
    main()