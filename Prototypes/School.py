"""
    Made by Angelo Battaglia (github.com/angelobattaglia)
    2021
    Licence: GPL
"""
import numpy as np
import scipy as sp
import Subject as sj
import Classe as cl
import Teacher as tc

class School:
    """
    Constructor
    """
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    """
    Getter Methods
    """
    def __str__(self):
        return self.name + ' is ' + str(self.code)

    