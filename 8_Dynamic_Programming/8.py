# Jae Duk Seo - 500 633 241
import numpy as np

# INPUT - Must be np.array - 2D
def Jae_Floyde(matrix = None):
	(width, height) = matrix.shape

	D = matrix

	for k in range(0,width):
		for i in range(0,width):
			for j in range(0,width):
				D[i,j] = min(D[i,j],D[i,k] + D[k,j])

	return D
m  = np.array( [ [1,32,3],
				 [422,522,6],
				 [-7,8,78]
				] )
print "\n8.12 Floyd algo - and the created Matirx : \n" , m
print "The result of Floyde Algo : \n",Jae_Floyde(m)







# ----- END OF THE CODE -------