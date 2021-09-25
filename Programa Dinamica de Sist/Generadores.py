#from sympy.core.singleton import S
from TransformacionesSRL import transf_cilindricas, transf_esfericas, transf_angulos
#from sympy.physics.vector import *

x = 0.0
y = 0.0
z = 0.0
SRG = [x, y, z]

class Particula:
    id = None
    masa = 0.0
    r = [0.0, 0.0, 0.0]
    x1 = 0.0
    y1 = 0.0
    z1 = 0.0
    SRL = [x1, y1, z1]
    
    def __init__(self, M, R, lista_xyz):
        self.masa = M
        self.r = R
        self.rSL_XYZ = lista_xyz


class CuerpoRigido:
    id = None
    masa = 0.0
    Inercia = None
    r = [0.0, 0.0, 0.0]
    orientacion = [0.0, 0.0, 0.0]
    x1 = 0.0
    y1 = 0.0
    z1 = 0.0
    SRL = [x1, y1, z1]
    
    def __init__(self, M, In, R, O, lista_xyz):
        self.CRmasa = M
        self.CRinercia = In
        self.CRr = R
        self.CRo = O
        self.CRrSL_XYZ = lista_xyz

    def transf_cilind():
        S1 = []
        for i in range(3):
            S1.append(self.CRrSL_XYZ[i])
            
        S2 = transf_cilindricas(S1)
        return S2


cuerpo_1  = CuerpoRigido(0, 0, 0, 0, [5, 3, 3])
S1 = []
for i in range(3):
    S1.append(cuerpo_1.CRrSL_XYZ[i])
    print(cuerpo_1.CRrSL_XYZ[i])
    
S2 = transf_angulos(S1, 0.54)
print(S2)
