import numpy as np

vecteur = np.arange(1, 10)  
print("Vecteur :", vecteur)

matrice = vecteur.reshape((3, 3))
print("Matrice 3x3 :\n", matrice)

print("Shape :", matrice.shape)
print("Size  :", matrice.size)

matrice_auto = vecteur.reshape((3, -1))
print("Shape auto :", matrice_auto.shape)
