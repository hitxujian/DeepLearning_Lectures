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

one3 = np.arange(0, 50, 5)
j = 0
for i in one3:
	Z = sigmoid(X, Y, 0, 25, i)
	#Z1 =  sigmoid(X, Y, 1, 100, -200)
	#Y1 = sigmoid(X, Y, 100, 1, 200)
	#Y2 = sigmoid(X, Y, 100, 1, -200)
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.2,
		                   linewidth=0, antialiased=False)
	ax.set_zlim(0, 1)

	ax.zaxis.set_major_locator(LinearLocator(10))
	ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
	#fig.colorbar(surf, shrink=0.5, aspect=5)
	#plt.savefig("bef.jpg")
	fig1 = plt.gcf()
	#plt.show()
	fig1.savefig(str(j)+".jpg")
	j = j+1
