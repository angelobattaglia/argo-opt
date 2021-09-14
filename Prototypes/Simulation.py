"""
    Made by Angelo Battaglia (github.com/angelobattaglia)
    2021
    Licence: GPL
"""

import School as sc
import Subject as sj
import Classe as cl
import Teacher as tc

if __name__ == '__main__':
    a1 = sc.School("Scuola Uno", 42)
    print(a1.__str__())
    a2 = sc.School("Scuola Due", 44)
    print(a2.__str__())

    cl1 = cl.Classe(3, 'D', 'Scientifico', '3D', 'Principale', 4, 7, [[1,1,0,0,0,0,0],
                                                                        [1,1,0,0,0,0,0],
                                                                        [1,1,0,0,0,0,0],
                                                                        [1,1,0,0,0,0,0],
                                                                        [1,1,0,0,0,0,0],
                                                                        [1,1,0,0,0,0,0]
                                                                         ])
    print("\nHere's the information about the class:")
    print(cl1.infoClasse())

    print("\nThe following is a numpy matrix of the Orario Scolastico:")
    print(cl1.giveOrarioAsMatrixNP())

    tc1 = tc.Teacher('Battaglia', 'Marco', 'BM', 'BTTMRC67R1002', 18, 4, 7, [[1,1,0,1,1,0,0],
                                                                        [1,1,0,0,1,0,0],
                                                                        [1,1,0,1,0,0,0],
                                                                        [1,1,0,0,1,0,0],
                                                                        [1,1,0,1,0,0,0],
                                                                        [1,1,0,0,1,0,0]
                                                                         ], 2, 3, 2, 4)
    print("\nHere's the information about the Teacher:")
    print(tc1.infoTeacher())
    print(tc1.infoTeacherUD())
    print(tc1.infoExtraContraints())