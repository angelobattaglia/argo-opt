"""
    Made by Angelo Battaglia (github.com/angelobattaglia)
    2021
    Licence: GPL
"""

import numpy as np
import scipy as sp
import School as sc
import Subject as sj
import Classe as cl

class Teacher:
    # Constructor
    def __init__(self, Surname, Name, IDteacher, CodiceFiscale, totUD, minUD, maxUD, orario, constraint1, constraint2, constraint3, constraint4):
        # Basic Informations
        self.surname = Surname
        self.name = Name
        self.IDteacher = IDteacher
        self.CodiceFiscale = CodiceFiscale
        # Totale U.D. a disposizione
        self.totUD = totUD
        # Availability
        self.minUD = minUD
        self.maxUD = maxUD
        # The following must be a matrix
        self.orario = orario
        # Extra Constraints
        ## N. Complessivo Giorni liberi Settimanali
        self.constraint1 = constraint1
        ## Max numero U.D. senza interruzione
        self.constraint2 = constraint2
        ## Min numero U.D. senza interruzione
        self.constraint3 = constraint3
        ## U.D. mutualmente esclusive
        self.constraint4 = constraint4

    """
    Convert the orario into a numpy array and return it as a numpy matrix
    """
    def giveOrarioAsMatrixNP(self):
        conversion = np.array(self.orario)
        return np.asmatrix(conversion)

    """
    Getter methods
    """
    def formatOrario(self):
        weekdays = ['monday','tuesday','Wednesday','thursday','friday','saturday','sunday']
        formattedoutput = {}
        for i in range(0,6):
            formattedoutput[i] = {weekdays[i]: self.orario[i]}
        return formattedoutput

    """
    Getter methods
    """
    def infoTeacher(self):
        return 'Surname: ' +  str(self.surname) + '\nName: ' + self.name + '\nID' + self.IDteacher + '\nCodice Fiscale:' + self.CodiceFiscale +  '\nOrario:' + str(self.formatOrario())

    def infoTeacherUD(self):
        return 'totUD: ' +  str(self.totUD) + '\nMinUD: ' + str(self.minUD) + '\nMaxUD: ' + str(self.maxUD)
                
    def infoExtraContraints(self):
        return 'Free Days Weekly: ' + str(self.constraint1) + '\nMax Didactical Units Without Interruption: ' + str(self.constraint2) + '\nMin Didactical Units Without Interruption: ' + str(self.constraint3) + '\nDidactical Units Mutually Exclusive: ' + str(self.constraint4) 