import numpy as np


tableau_float32 = np.array([1, 2, 3], dtype=np.float32)
print("tableau_float32 :", tableau_float32)
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
