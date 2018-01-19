from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import os


def get_points() :
	X = np.random.rand(60) * 2
	Y = np.random.rand(60) * 2

	for x, y in zip(X,Y) :

		if x + y >= 2.3 :
			print ("\\filldraw[blue] (%f,%f) circle (2pt);" %(x, y))
		if x + y < 1.7 :
			print ("\\filldraw[red] (%f,%f) circle (2pt);" %(x, y))
	
def print_boolean_table() :
	row1 = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1] 	
	row2 = [0,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1]
	row3 = [1,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1]
	row4 = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
	sequence = [3,3,4,6,8,9,10,11,12,7,13,14,15,16,17,18,19,5]

	for row in [row1, row2, row3, row4] :
		text = ''
		for i,x in enumerate(row) :
				text = text + '\\onslide<' + str(sequence[i]) + '->{' + str(x) + '}&' 
		print (text)


if __name__ == '__main__' :
	#get_points()
	print_boolean_table()