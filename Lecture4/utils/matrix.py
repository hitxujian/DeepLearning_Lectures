import sys

prefix="\\frac{\\partial \\mathscr{L}(\\theta)}{\\partial W_{"
suffix="}}"
mat = ""
for i in range(5) :
	for j in range(5) :
		for k in range(5) :
			if (j==0 and k < 1) or  (j==4 and k<2) :
				ind = str(i) + str(j) +str(k)
				mat += prefix + ind + suffix
				print (prefix + ind + suffix)
			elif j == 1 :
				print ("..")
				mat += ".."
		mat += "\n"
