# Jae Duk Seo - 500 633 241

def Jae_Insertion_Sort(array = None):

	for i in range(1, len(array)):
		v = array[i]
		j = i - 1
		while j >= 0 and array[j] > v :
			array[j+1] = array[j]
			j = j - 1
		array[j+1] = v
	return array
a = [3,4,2,56,23,4,3,-9]
print "\n5.2 Insertion Sort and the array that I created : ", a
print "The Sorted array : ", Jae_Insertion_Sort(a)
# -------------------------

print "\nJae : For most part the decrease and conquer part was more hand written solved problems. "
print "Hope you guys good luck!"







#------- END OF THE CODE --------