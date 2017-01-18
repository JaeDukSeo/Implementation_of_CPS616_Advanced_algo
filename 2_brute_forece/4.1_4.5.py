# Jae Duk Seo 500 633 241


def Jae_Selection_sort(array = None):
	current_minval = 0
	for i in range(0,len(array)-1):
		current_minval = i
		for j in range(i+1,len(array)):
			if array[j] < array[current_minval]:
				current_minval = j
		temp = array[current_minval]
		array[current_minval] = array[i]
		array[i] = temp

	return array

print "1. Selection Sort "
array = [29,3,4,2,-3,2,0,0.002]
print Jae_Selection_sort(array)
# ---------------------------------

def Jae_Bruteforcestring(text = None, pattern = None):
	if len(pattern) > len(text):
		return False
	n = len(text)
	m = len(pattern)
	for i in range(0,n-m):
		j = 0
		while j<m and pattern[j] == text[i+j]:
			j = j + 1
		# The length of the pattern equals the length that is found in the text string 
		# That means the text contains the pattern since one of the condition is  pattern[j] == text[i+j]
		if j == m:
			return True

	return False

print "\n2. Brute Force String patter"
text = 'This is my text'
pattern = "is"
print Jae_Bruteforcestring(text,pattern)
# ---------------------------------
import time
from random import randint
def Jae_poly(point =None, n = None ):
	random_const = [randint(0,9) for p in range(0,n)]
	print 'Constants are : ', random_const[::-1]
	p = 0.0
	for i in range(n-1,-1,-1):
		power = 1
		for j in range(0,i):
			power = power * point
		p = p + random_const[i] * power

	return p
print "\n3. Poly no improvement"
start_time = time.time()
print Jae_poly(3,500), " answer with 500 Constants"
print("--- %s seconds ---" % (time.time() - start_time))
# ---------------------------------
def Jae_poly_improve_one(point= None, n = None):
	random_const = [randint(0,9) for p in range(0,n)]
	print 'Constants are : ', random_const[::-1]
	p = random_const[0]
	power = 1
	for i in range(1,n):
		power = power * point 
		p = p + random_const[i] * power
	return p
print "\n3.1 Poly with one improvement"
start_time = time.time()
print Jae_poly_improve_one(3,500), " answer with 500 Constants"
print("--- %s seconds ---" % (time.time() - start_time))
# ---------------------------------

def Jae_Poly_final(points= None, n = None ):
	random_const = [randint(0,9) for p in range(0,n)]
	print 'Constants are : ', random_const[::-1]
	p = random_const[n-1]
	for i in range(n-2,-1,-1 ):
		p = p * points + random_const[i]
	return p

print "\n3.2 Poly with final improvement"
start_time = time.time()
print Jae_Poly_final(3,500), " answer with 500 Constants"
print("--- %s seconds ---" % (time.time() - start_time))
# ---------------------------------
import math
def Jae_Bruteforce_point(points = None):
	dmin  = float("inf")
	for i in range(0,len(points) - 1):
		for j in range(i+1,len(points)):
			d = math.sqrt( (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2 )
			if d< dmin:
				dmin  = d
				index1 = i
				index2 = j
	return index1,index2 

print "\n4.4 Brute force closetest length"
points = [ (1,2),( 3000 ,4),(455,399),(5,6) ]
print "I made points that look like ", points, " so the expected output is first point and last point - which is 0 and 3"
print Jae_Bruteforce_point(points), ' : Are the closest points'
# ---------------------------------

def Jae_Max_element(array = None):
	maxval = array[0]

	for i in range(1,len(array)):
		if array[i] > maxval:
			maxval = array[i]

	return maxval

print "\n4.5 Max Element - Exhaustive Search"
array = [2,3,4,9,2,90,44]
print "The array that I have : ", array
print "The max element that I found : ",Jae_Max_element(array)
# ---------------------------------



# ---- END OF THE CODE ------------------