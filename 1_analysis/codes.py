#Jae Duk Seo - CPS 616 - implementation of algo 


# -------------------------------
def MaxElement(array = None):
	# Set it to the first array element
	maxval = array[0]
	for i in range(1,len(array)):
		if array[i] > maxval:
			maxval = array[i]
	return maxval

print '1. Max Element'
array = [0,2,3,5,882,2,1,5,2,3,90]
print MaxElement(array)

# -------------------------------
def UniqueElement(array = None ):
	for i in range(0, len(array) - 1 ):
		for j in range(i+1,len(array)):
			if array[i] == array[j]:
				return False 
	return True

print "2. Unique"
array = [1,2,3,4,5,9,0]
print UniqueElement(array)

# -------------------------------
import numpy as np
# Source: https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm
# Just basic simple Matrix multiplication 
def MatrixMulti(m1=None,m2=None):
	print m1
	print m2
	C = np.zeros(m1.shape)
	height,width = m1.shape
	for i in range(0,height):
		for j in range(0,width):
			C[i][j] = 0
			for k in range(0,width):
				C[i][j] = C[i][j] + m1[i][k] * m2[k][j] 

	return C

print "3. Matirx Multiplecation"
m1 =np.array([ [2,2,0],[3,2,2],[1,5,0] ])
m2 =np.array([ [0,2,0],[4,3,0],[2,1,0]  ])
print MatrixMulti(m1,m2)
print "For validation go to this website: http://matrix.reshish.com/multCalculation.php"

# -------------------------------
import math
def BinRec(positive = None):
	if positive == 1:
		return 1
	else:
		return BinRec(math.floor(positive/2)) + 1

print "4. Binary Rep - Jae: I have no idea what this algo is doing, Have to ask Prof. Quigley"
try:
	print BinRec(int(raw_input("Please input positive decimal : ")))
except:
	print 'Input error - Try again with positive decimal integer!'

# -------------------------------
def f(number = None):
	if number == 0:
		return 1
	else:
		return f(number - 1) * number
print "5. n factorial"
try:
	print f(long(raw_input("Please input positive decimal : (Note if the number is too high, cannot compute!)")))
except:
	print 'Input error - Try again with positive decimal integer!'
# -------------------------------





# -------END OF CODE-------