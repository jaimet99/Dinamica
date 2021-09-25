cuerpo_1  = CuerpoRigido(0, 0, 0, 0, [5, 3, 3])
S1 = []
for i in range(3):
    S1.append(cuerpo_1.CRrSL_XYZ[i])
    print(cuerpo_1.CRrSL_XYZ[i])
    
S2 = transf_angulos(S1, 0.54)
print(S2)