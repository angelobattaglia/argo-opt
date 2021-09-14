"""
    Made by Angelo Battaglia (github.com/angelobattaglia)
    2021
    Licence: GPL
"""

import numpy as np
import scipy as sp
import School as sc
import Subject as sj
import Teacher as tc

class Classe:
    # Constructor
    def __init__(self, fascia, sezione, specialization, ID, sede, minUD, maxUD, orario):
        self.fascia = fascia
        self.sezione = sezione
        self.specialization = specialization
        self.ID = ID
        self.sede = sede
        self.minUD = minUD
        self.maxUD = maxUD
        # The following must be a matrix
        self.orario = orario

    # Convert the orario into a numpy array and return it as a numpy matrix
    def giveOrarioAsMatrixNP(self):
        conversion = np.array(self.orario)
        return np.asmatrix(conversion)

    # Getter methods
    def infoClasse(self):
        return 'Classe: ' +  str(self.fascia) + '\nSezione: ' + self.sezione + '\nSpecializzazione: ' + str(self.specialization) + '\nID: ' + self.ID + '\nSede: ' + self.sede + '\nminUD: ' + str(self.minUD) + '\nmaxUD: ' + str(self.maxUD) + '\nOrario: ' + str(self.orario)
