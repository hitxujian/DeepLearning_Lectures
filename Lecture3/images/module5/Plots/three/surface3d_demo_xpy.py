from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math

def sigmoid(x,y,w1,w2,b):
	val1 = w1*x
	val2 = w2*y
	val3 = np.add(val1,val2)
	val3 = val3 + b
	val = 1.0/(1 + np.exp(-val3))
	return val
 

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
print(X.shape, Y.shape)


Z11 = sigmoid(X, Y, 100, 0, -200)
Z21 = sigmoid(X, Y, 100, 0, 200)
Z1 = Z21 - Z11
Z12 = sigmoid(X, Y, 0, 100, -200)
Z22 = sigmoid(X, Y, 0, 100, 200)
Z2 = Z22 - Z12
Z = Z1 + Z2
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.7,
	                   linewidth=0, antialiased=False)
ax.set_zlim(0, 2)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#fig.colorbar(surf, shrink=0.5, aspect=5)
#plt.savefig("bef.jpg")
fig1 = plt.gcf()
#plt.show()
fig1.savefig("xpyjoin.jpg")
