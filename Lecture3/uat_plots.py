from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


import numpy as np
from numpy import ma
import matplotlib.pyplot as plt

x = np.arange(0, 2, 0.04)
y = 0.35 + 232.37 * x -5321 * x *x + 485268 * np.power(x, 3)
y = y/(np.sum(y))


plt.step(x, y)
plt.plot(x, y)
#y -= 0.5
#plt.step(x, y, where='mid', label='mid')

#y -= 0.5
#plt.step(x, y, where='post', label='post')

#y = ma.masked_where((y0 > -0.15) & (y0 < 0.15), y - 0.5)
#plt.step(x, y, label='masked (pre)')

plt.legend()

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.savefig('test.png', bbox_inches='tight')

"""
for w1 in range(10) :
	for w2 in range(-10):

		fig = plt.figure()
		ax = fig.gca(projection='3d')
		X = np.arange(-5, 5, 0.25)
		Y = np.arange(-5, 5, 0.25)
		X, Y = np.meshgrid(X, Y)
		#R = np.sqrt(X**2 + Y**2)
		#Z = np.sin(R)
		Z = 1.0 / (1.0 + np.exp(-(X + Y))) 
		Z -= 1.0 / (1.0 + np.exp(-(X + Y - 5)))
		surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
		                       linewidth=0, antialiased=False, alpha=0.1)
		ax.set_zlim(-1.01, 1.01)

		ax.zaxis.set_major_locator(LinearLocator(10))
		ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

		fig.colorbar(surf, shrink=0.5, aspect=5)
		ax.view_init (elev=0, azim=-40)           # elevation and angle
		plt.savefig('figure.' + str(20) + '_' + str(-angle) + '.png', bbox_inches='tight')

"""
#plt.show()