'''
    Made by Angelo Battaglia (https://github.com/angelobattaglia)
    2021
    Licence: GPL
'''
import numpy as np
import scipy as sp
import Subject as sj
import Classe as cl
import Teacher as tc

class GeneticAlgorithm:

    # Example of passing an object to a constructor of another class and then working 
    # with its methods:
    #def __init__(self, Subject):
    #    self.Subject = Subject

    def __init__(self, Classes, Teachers):
        self.Classes = Classes
        self.Teachers = Teachers
        # self.School = School
        # self.Subjects = Subjects


