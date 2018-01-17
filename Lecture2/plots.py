from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import os


def f(w1,w2,x1,x2) : #sigmoid with parameters w,b
	return w1*x1 + w2*x2 - 1


def error (W1, W2) :
	X1 = [0,0,1,1]
	X2 = [0,1,0,1]
	Y = [0,1,1,1]
	err = 0.0
	errors = np.zeros((256, 256))

	for i in range(256) :
		for j in range (256) :
			w1 = W1[i][j]	
			w2 = W2[i][j]
			err = 0
			for x1,x2,y in zip(X1,X2,Y) :
				fx = f(w1, w2, x1, x2)
				if y ==0 and fx >= 0 :
					err+=1
				if y ==1 and fx < 0 :
					err+=1
			errors[i][j] = err 		
	return errors		

def plot_error_surface(plot_contour=False, id=1) :
	w1 = np.linspace(-5, 5, 256)            # points in the x axis
	w2 = np.linspace(-5, 5, 256)            # points in the y axis
	W1, W2 = np.meshgrid(w1, w2)          # create the "base grid"
	print (W1)
	print (W2)
	E = error(W1, W2)                   # points in the z Axis

	fig = plt.figure(id)

	ax = fig.gca(projection='3d')         # set the 3d axes

	surf = ax.plot_surface(X=W1, Y=W2, Z=E, rstride=3, cstride=3, alpha=0.3, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


	ax.set_xlabel('w_1')
	ax.set_xlim(-5, 5)
	ax.set_ylabel('w_2')
	ax.set_ylim(-5, 5)
	ax.set_zlabel('error')
	ax.set_zlim(0, 4)
	#ax.set_title('Gradient descent on the error surface', va='bottom')
	ax.view_init (elev=25, azim=-20)           # elevation and angle
	ax.dist=12                                # distance

	fig.colorbar(surf, orientation='horizontal', shrink=0.75, aspect=10)

	plt.savefig('images/or_error_surface.png', bbox_inches='tight')
	
	return ax

if __name__ == '__main__' :
	plot_error_surface()
