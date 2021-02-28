# Numpy - a library for scientific computation
# basis for pandas

import numpy as np


a = np.array([0, 1, 2, 3, 4])

print(a)
## type
print(type(a))
## size
print(a.size)
## dimention
print(a.ndim)
## shape - touple - size in each dimention
print(a.shape)
## slicing
#print(a[1:4])
## assign new values to indeces
a[2:4] = 200,300
print(a)


print("---- vector Operations")
print("+++ addition")
u = np.array([2,1])
v = np.array([3,1])
a = u + v
print(type(a))
print(a.dtype)
print(a)
print(a.ndim) ## dimensions
print(a.shape)

print("+++ subtraction")
b = u - v
print(b)

print("+++ multiplication")
c = 2 * u
print(c)

print("+++ Product")
d = u * v
print(d)

print("+++ Dot Product")
e = np.dot(u,v)
print(e)

print("+++ Broadcasting")
f = u + 1
print(f)

print("--------- Universal Functions")

print("+++ mean")
mean_u = u.mean()
print(mean_u)

print("+++ find max in an array")
max_u = u.max()
print(max_u)

print("+++ line space")
ls = np.linspace(-2,2,num=9)
print(ls)


print("------ Displaying as plot")
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

import matplotlib.pyplot as plt
# %matplotlib inline
plt.plot(x, y)