import numpy as np

tableau_1d = np.array([1, 2, 3, 4, 5])
print("Tableau 1D :", tableau_1d)

tableau_2d = np.array([[1, 2, 3],
                       [4, 5, 6]])
print("Tableau 2D :\n", tableau_2d)

zeros = np.zeros((2, 3))
print("Zeros :\n", zeros)

ones = np.ones((3, 2))
print("Ones :\n", ones)

progression = np.arange(0, 10, 2)
print("np.arange :", progression)

linspace = np.linspace(0, 1, 5)
print("np.linspace :", linspace)

print("tableau_1d + 5 :", tableau_1d + 5)

print("\n--- Inspection tableau_1d ---")
print("dtype :", tableau_1d.dtype)
print("ndim  :", tableau_1d.ndim)
print("shape :", tableau_1d.shape)
print("size  :", tableau_1d.size)

print("\n--- Inspection tableau_2d ---")
print("dtype :", tableau_2d.dtype)
print("ndim  :", tableau_2d.ndim)
print("shape :", tableau_2d.shape)
print("size  :", tableau_2d.size)

print("\n--- Inspection zeros ---")
print("dtype :", zeros.dtype)
print("ndim  :", zeros.ndim)
print("shape :", zeros.shape)
print("size  :", zeros.size)

print("\n--- Inspection ones ---")
print("dtype :", ones.dtype)
print("ndim  :", ones.ndim)
print("shape :", ones.shape)
print("size  :", ones.size)

print("\n--- Inspection progression ---")
print("dtype :", progression.dtype)
print("ndim  :", progression.ndim)
print("shape :", progression.shape)
print("size :", progression.size)

print("\n--- Inspection linspace ---")
print("dtype :", linspace.dtype)
print("ndim  :", linspace.ndim)
print("shape :", linspace.shape)
print("size :", linspace.size)

exemple_promotion = np.array([1, 2, 3.0])
print("\nPromotion dtype :", exemple_promotion, "dtype =", exemple_promotion.dtype)

print("Type Python :", type(tableau_1d))
print("Dtype interne :", tableau_1d.dtype)


vecteur = np.arange(1, 10)
print("\nVecteur :", vecteur)

matrice = vecteur.reshape((3, 3))
print("Matrice 3x3 :\n", matrice)
print("Shape :", matrice.shape)
print("Size  :", matrice.size)

matrice_auto = vecteur.reshape((3, -1))
print("Shape auto :", matrice_auto.shape)

tableau_float32 = np.array([1, 2, 3], dtype=np.float32)
print("\ntableau_float32 :", tableau_float32)
print("dtype :", tableau_float32.dtype)

tableau_int32 = tableau_float32.astype(np.int32)
print("tableau_int32 :", tableau_int32)
print("dtype :", tableau_int32.dtype)

print("Mémoire float32 :", tableau_float32.nbytes, "octets")
print("Mémoire int32   :", tableau_int32.nbytes, "octets")

identite = np.eye(4)
print("\nMatrice identité (4x4) :\n", identite)

constant = np.full((2, 2), 7)
print("\nTableau constant (2x2) rempli de 7 :\n", constant)

test_reshape = np.arange(12).reshape((4, 3))
print("\nnp.arange(12).reshape((4, 3)) :\n", test_reshape)

print("\nmatrice * 10 :\n", test_reshape * 10)

vecteur = np.arange(1, 10)
print("\nnp.sqrt(vecteur) :\n", np.sqrt(vecteur))


alist = [0] * 6
array_np = np.zeros(6)

print("\nalist =", alist, "type =", type(alist))
print("np.zeros(6) =", array_np, "type =", type(array_np))
print("array_np + 5 =", array_np + 5)

lin = np.linspace(0, 1, 5)
print("np.linspace(0,1,5) :", lin)

tableau_9 = np.arange(9)
print("\nTableau 9 éléments :", tableau_9)

try:
    mauvais = tableau_9.reshape((4, 3))
except ValueError as e:
    print("Erreur reshape :", e)

tableau = np.array([1, 2, 3])
liste = tableau.tolist()
print("tableau.tolist() :", liste)

tableau_reconstruit = np.array(liste)
print("np.array(liste)  :", tableau_reconstruit)

