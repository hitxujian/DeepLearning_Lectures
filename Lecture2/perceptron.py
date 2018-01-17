from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import os


def f(w1,w2,x1,x2) : #sigmoid with parameters w,b
	return w1*x1 + w2*x2 


def run_perceptron (w1, w2) :
	x1 = [-0.5, 0.5, 3, -1.5, -0.5, 0.5]
	x2 = [1.2, 2, 1, 0.5, -2, -2]
	y = [1, 1, 1, 0, 0, 0]

	x=np.arange(6)
	np.random.shuffle(x)

	while True :
		error = 0
		for j,i in enumerate(x) :
			print ("\onslide<%d->{\draw[-{>[length=3]}] (0,0) -- (%f, %f);}" % (j, w1, w2))

			fx = f(w1, w2, x1[i], x2[i])

			if y[i] == 0 :
				if fx >= 0 :
					print ("\item<%d>Pick n%d, apply correction $\mathbf{w} = \mathbf{w} - \mathbf{x}$ " %(i, i+1))
					w1 -= x1[i]
					w2 -= x2[i]
					error +=1
				else :
					print ("\item<%d>Pick n%d, no correction needed $ \because \mathbf{w\cdot x < 0}$ " %(i, i+1))

			if y[i] == 1:
				if fx < 0 :
					print ("\item<%d>Pick p%d, apply correction $\mathbf{w} = \mathbf{w} + \mathbf{x}$ " %(i, i+1))
					w1 += x1[i]
					w2 += x2[i]
					error +=1
				else :
					print ("\item<%d>Pick p%d, no correction needed $ \because \mathbf{w\cdot x \geq 0}$ " %(i, i+1))
					

			#print (w1, w2)	

		if error == 0 :
			break		

		

if __name__ == '__main__' :
	run_perceptron(-2, -2)
