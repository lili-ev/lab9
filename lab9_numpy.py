import numpy as np
tableau = np.array([1, 2, 3, 4, 5])
print("Tableau 1D :", tableau)
print("dtype :", tableau.dtype)
print("ndim  :", tableau.ndim)  
print("shape :", tableau.shape)  
print("size  :", tableau.size) 

tableau_2d = np.array([[1, 2, 3],
                       [4, 5, 6]])
print("Tableau 2D :\n", tableau_2d)
print("dtype :", tableau.dtype)
print("ndim  :", tableau.ndim)  
print("shape :", tableau.shape)  
print("size  :", tableau.size) 

zeros = np.zeros((2, 3))
print("Zeros :\n", zeros)
print("dtype :", tableau.dtype)
print("ndim  :", tableau.ndim)  
print("shape :", tableau.shape)  
print("size  :", tableau.size) 


ones = np.ones((3, 2))
print("Ones :\n", ones)
print("dtype :", tableau.dtype)
print("ndim  :", tableau.ndim)  
print("shape :", tableau.shape)  
print("size  :", tableau.size) 


progression = np.arange(0, 10, 2)  
print("np.arange :", progression)
print("dtype :", tableau.dtype)
print("ndim  :", tableau.ndim)  
print("shape :", tableau.shape)  
print("size  :", tableau.size) 

 