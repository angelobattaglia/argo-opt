"""
    Made by Angelo Battaglia (github.com/angelobattaglia)
    2021
    Licence: GPL
"""
import numpy as np
import scipy as sp
import School as sc
import Classe as cl
import Teacher as tc

class Subject:
    # Constructor
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    # Getter methods
    def getName(self):
        return self.name + ' is ' + str(self.code)

    def getCode(self):
        return self.name + ' is ' + str(self.code)
    