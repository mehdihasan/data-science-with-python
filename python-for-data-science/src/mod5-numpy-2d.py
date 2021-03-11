import numpy as np

a = [[13,34,34], [12,23,54], [65,34,45]]
A = np.array(a)
print(A)

## print dimension
print("--- DIMENSION")
print(A.ndim)


## print shape
print("--- SHAPE")
print(A.shape)

## total items
print(A.size)

## A[row:column]
print(A[0:1])
print(A[0:2,2])


## exam
a=np.array([0,1])
b=np.array([1,0])
print(np.dot(a,b))


a=np.array([1,1,1,1,1])
print(a+10)