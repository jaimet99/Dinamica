# Se importa una libreria para el calculo de matricesu
import numpy as np
import sympy as sp
import calculadora as cl



def transf_angulos(S1, ang):
    # A traves de esta libreria se calcula el produto punto entre matrices, 
    # para obtener los valores de a nueva matriz
    Matriz_X = [[np.cos(ang), np.sin(ang), 0], [-np.sin(ang),  np.cos(ang), 0], [0, 0, 1]]

    Matriz_Y = [[np.cos(ang), 0,  np.sin(ang)], [0, 1 ,0], [-np.sin(ang), 0, np.cos(ang)]]

    #Matriz_Z = [[0, 0, 1], [0, np.cos(ang), - np.sin(ang)], [0, np.sin(ang), - np.cos(ang)]]
    #vector = []
    #for i in range(3):
     #   lista = []
      #  for j in range(3):
       #     matriz = Matriz_X[i][j]
        #    w = int(S1[i])
         #   a = matriz * w
          #  lista.append(a)
    S2 = Matriz_X * int(S1[0])
    #S2 = Matriz_Y * S1
    #S2 = Matriz_Z * S1

    return S2
    



def transf_esfericas(S1):
    #Mediante otra libreria se obtienen las coordenadas esfericas de ciertas
    #coordenadas cartesianas.
    x = int(S1[0])
    y = int(S1[1])
    z = int(S1[2])

    r_esferica = np.sqrt((x**2)+(y**2)+(z**2))
    fi_esferica = np.arctan(y/x)
    teta_esferica = np.arctan((np.sqrt((x**2)+(y**2)))/z)
    S2 = [r_esferica, fi_esferica, teta_esferica]

    return S2

def transf_cilindricas(S1):
    #Mediante otra libreria se obtienen las coordenadas esfericas de ciertas
    #coordenadas cartesianas.
    x = int(S1[0])
    y = int(S1[1])
    z = int(S1[2])
    w = y/x

    r_cilind = np.sqrt(x**2 + y**2)
    teta_cilind = np.arctan(w)
    z_cilind = z
    S2 = [r_cilind, teta_cilind, z_cilind]

    return S2
