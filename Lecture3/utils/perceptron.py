from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import os


def f(w0, w1,w2,x1,x2) : #sigmoid with parameters w,b
	return w1*x1 + w2*x2 + w0

def find_points(w0, w1, w2) :

	x2 = (1.0*w1 - w0) / w2
	x1 = (1.0*w2 - w0) / w1
	#x1 = -w0/w1
	#x2 = -w0/w1
	print ("\\draw[thick,->] (%f,-1) -- (-1,%f);" %(x1, x2)) 

def run_perceptron (w0, w1, w2) :
	x0 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
	x1 = [1.717248,1.022337,0.929218,1.256599,1.917421,1.552910,0.476688,1.139669,1.994183,0.611827,1.954791,0.113127,1.547272,1.667688,0.108270,1.551238,0.550644,1.326191,0.285269,0.645487,0.715271,0.239037,1.707163,0.663682,0.512817,1.542905,1.928409,0.430763,0.411993,0.951387,0.001601,0.983530,0.612532,1.217355,0.398657,0.452156,0.458527,1.977895,0.217980,0.075486,1.872187,1.142016,1.411278,1.951329,0.543241]
	x2 = [1.148263,1.844630,1.449012,1.328157,1.041134,0.757361,0.993158,1.889055,1.472244,0.938297,0.598560,1.025315,1.235639,0.664851,0.066074,0.091185,0.461861,1.171462,0.166320,1.900755,0.514446,0.110620,1.213513,1.796715,0.075660,0.897760,0.514645,1.999726,0.218422,0.725352,1.490619,0.364934,0.194346,1.773029,0.261244,1.890002,0.384611,1.687690,0.748811,1.486788,1.761516,1.716686,1.734101,1.101424,0.052208]
	y = [0,1,1,0,1,1,0,1,0,0,1,0,1,1,1,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,0,1,0,1,1,0,1,1,1,1,0]
	#y = [1,1,1,1,1,1,0,1,1,0,1,0,1,1,0,0,0,1,0,1,0,0,1,1,0,1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,1,1,1,0]

	#w0 = np.mean(x0)
	#w1 = np.mean(x1)
	#w2 = np.mean(x2)
	print (len(x1))
	x=np.arange(45)
	np.random.shuffle(x)
	k=0
	itera = 0
	min_iter = 0
	min_error = 100
	while itera < 50000 :
		error = 0
		itera +=1
		for j,i in enumerate(x) :
			#print ("\onslide<%d->{\draw[-{>[length=3]}] (0,0) -- (%f, %f);}" % (j, w1, w2))

			fx = f(w0, w1, w2, x1[i], x2[i])

			if y[i] == 0 :
				if fx >= 0 :
					#print ("\item<%d>Pick n%d, apply correction $\mathbf{w} = \mathbf{w} - \mathbf{x}$ " %(i, i+1))
					w0 -= x0[i]
					w1 -= x1[i]
					w2 -= x2[i]
					error +=1
				else :
					k+=1
					#print ("\item<%d>Pick n%d, no correction needed $ \because \mathbf{w\cdot x < 0}$ " %(i, i+1))

			if y[i] == 1:
				if fx < 0 :
					#print ("\item<%d>Pick p%d, apply correction $\mathbf{w} = \mathbf{w} + \mathbf{x}$ " %(i, i+1))
					w0 += x0[i]
					w1 += x1[i]
					w2 += x2[i]
					error +=1
				else :
					k+=1
					#print ("\item<%d>Pick p%d, no correction needed $ \because \mathbf{w\cdot x \geq 0}$ " %(i, i+1))
					
		#print (error)		
			#print (w1, w2)	
		find_points(w0, w1, w2)
		if error < min_error :
			min_error = error
			min_iter = itera
		print(w0, w1, w2, error, min_error, min_iter)	
		if error == 0 :
			break		

		

if __name__ == '__main__' :
	run_perceptron(0, 0, 0)
