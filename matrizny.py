import numpy as np
A= np.array([[1,2],[3,4]])
B= np.array([[5,6],[7,8]])
#suma de elementos
suma = A+B
print("--suma A+B--")
print(suma)
#multiplicacion de elementos
prod_elem=A+B
print("--multiplcacion A*B--")
print(prod_elem)
#producto matricial
prod_mat=A@B
print(prod_elem)
#transpuesta)
transpuesta= A.T
print("trasnpuesta--A")
print(transpuesta)
#determine e inversa
det=np.linalg.det(A)
inv=np.linalg.inv(B)
print("determinante de A")
print(det)
print("inversa de A")
print(inv)