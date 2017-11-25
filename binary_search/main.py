
# performs binary search on input list
def binary_search(a,value):
	if len(a)==0: return False
	if len(a)==1:
		if a[0]==value: return True
		else:           return False

	mid=a[len(a)/2]
	if value==mid: return True 
	if value<mid:  return binary_search(a[:len(a)/2],value)
	if value>mid:  return binary_search(a[len(a)/2:],value)


# performs linear search on the input list
def linear_search(a,value):
	for elem in a:
		if elem==value: return True
	return False 

def create_array(size,max):
	from random import randint 
	return [randint(0,max) for _ in range(size)]


from time import time 

a=create_array(10000,10000)

t0=time()
linear_search(a,20000)
t1=time()
print "Linear Time: %0.5f" % (t1-t0)

t0=time()
a=sorted(a)
binary_search(a,20000)
t1=time()
print "Binary Time: %0.5f" % (t1-t0)


#a=[1,2,3,4,5,6,7,8,9]
#print binary_search(a,5)