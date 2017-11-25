
# merges two sorted arrays a & b
def merge(a,b):
	c=[]
	a_idx,b_idx=0,0
	while a_idx<len(a) and b_idx<len(b):
		if a[a_idx]<b[b_idx]:
			c.append(a[a_idx])
			a_idx+=1
		else:
			c.append(b[b_idx])
			b_idx+=1
	if a_idx==len(a): c.extend(b[b_idx:])
	else: 			  c.extend(a[a_idx:])
	return c 

# performs merge sort on the input array
def merge_sort(a):
	# a list of zero or one elements is sorted, by definition
	if len(a)<=1: return a 
	# split the list in half and call merge sort recursively on each half
	left,right = merge_sort(a[:len(a)/2]),merge_sort(a[len(a)/2:])
	# merge the now-sorted sublists
	return merge(left,right)

def create_array(size=10,max=50):
	from random import randint
	return [randint(0,max) for _ in range(size)]

a=create_array()
print a 
a=merge_sort(a)
print a