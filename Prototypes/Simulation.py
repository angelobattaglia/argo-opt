"""
    Made by Angelo Battaglia (github.com/angelobattaglia)
    2021
"""

import School as sc
import Subject as sj
import Classe as cl
import Teacher as tc
import GeneticAlgorithm as GA

if __name__ == '__main__':

    a1 = sc.School("Scuola Uno", 911)
    a2 = sc.School("Scuola Due", 666)

    cl1 = cl.Classe(3, 'D', 'Scientifico', '3D', 'Principale', 4, 7,   [[1,1,1,1,1,0,0],
                                                                        [1,1,1,1,1,0,0],
                                                                        [1,1,1,1,1,0,0],
                                                                        [1,1,1,1,1,0,0],
                                                                        [1,1,1,1,1,0,0],
                                                                        [1,1,1,1,1,0,0]
                                                                         ])
    cl2 = cl.Classe(4, 'D', 'Scientifico', '4D', 'Principale', 5, 5,   [[1,1,1,1,1,1,0],
                                                                        [1,1,1,1,1,1,0],
                                                                        [1,1,1,1,1,1,0],
                                                                        [1,1,1,1,1,1,0],
                                                                        [1,1,1,1,1,1,0],
                                                                        [1,1,1,1,1,1,0]
                                                                         ])
    cl3 = cl.Classe(3, 'D', 'Scientifico', '3D', 'Principale', 4, 7,   [[1,1,1,1,1,0,0],
                                                                        [1,1,1,1,1,0,0],
                                                                        [1,1,1,1,1,0,0],
                                                                        [1,1,1,1,1,0,0],
                                                                        [1,1,1,1,1,0,0],
                                                                        [1,1,1,1,1,0,0]
                                                                         ])
    
    tc1 = tc.Teacher('Battaglia', 'Marco', 'BM', 'BTTMRC67R1002', 18, 4, 7, [[1,1,1,1,1,0,0],
                                                                        [1,1,1,1,1,0,0],
                                                                        [1,1,1,1,0,0,0],
                                                                        [1,1,1,1,1,0,0],
                                                                        [1,1,1,1,0,0,0],
                                                                        [1,1,1,1,1,0,0]
                                                                         ], 2, 3, 2, 4)
    
    tc2 = tc.Teacher('Battaglia', 'Angelo', 'AB', 'ANBTTAC67R1002', 18, 4, 7, [[1,1,1,1,1,0,0],
                                                                        [1,1,1,1,1,0,0],
                                                                        [1,1,1,1,0,0,0],
                                                                        [1,1,1,1,1,0,0],
                                                                        [1,1,1,1,0,0,0],
                                                                        [1,1,1,1,1,0,0]
                                                                         ], 2, 3, 2, 4)
        # Printing the informations of the datas that are input
    print("\nHere's the information about the Schools:")
    print(a1.getInfo())
    print(a2.getInfo())
    print("\nHere's the information about the classes:")
    print(cl1.infoClasse())
    print("\nThe following is a numpy matrix of the Orario Scolastico:")
    print(cl1.giveOrarioAsMatrixNP())
    print("\nHere's the information about the first Teacher:")
    print(tc1.infoTeacher())
    print(tc1.infoTeacherUD())
    print(tc1.infoExtraContraints())
    
        # Testing the Genetic Algorithm:
    '''
        tc1 is the first teacher
        tc2 is the second teacher
        cl1 is the first class
        cl2 is the second class
        cl3 is the third class
        a1 is the first school
        a2 is the second school
    '''
    
    GEN_ALGO = GA.GeneticAlgorithm([cl1, cl2, cl3], [tc1, tc2])
    
    # GEN_ALGO.compute()
    # GEN_ALGO.plot()
