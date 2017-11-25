from random import randint

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


# applies quicksort to the input array, returns sorted array
def quicksort(a):
	if len(a)<=1: return a 

	smaller,equal,larger=[],[],[]
	pivot=a[randint(0,len(a)-1)]

	for x in a:
		if x<pivot:    smaller.append(x)
		elif x==pivot: equal.append(x)
		else:          larger.append(x)

	return quicksort(smaller)+equal+quicksort(larger)

def create_array(size=10,max=50):
	return [randint(0,max) for _ in range(size)]


times={'quick':[],'merge':[]}
n=[10,100,1000,10000,100000]
samples=5
from time import time 

for size in n:

	tot_time=0.0
	for _ in range(samples):
		a=create_array(size,size)
		t0=time()
		s=merge_sort(a)
		t1=time()
		tot_time+=(t1-t0)
	times['merge'].append(tot_time/float(samples))

	tot_time=0.0
	for _ in range(samples):
		a=create_array(size,size)
		t0=time()
		s=quicksort(a)
		t1=time()
		tot_time+=(t1-t0)
	times['quick'].append(tot_time/float(samples))

print "n\tQuicksort\tMergesort"
print 40*"_"
for i,size in enumerate(n):
	print "%d\t%0.5f \t%0.5f"%(
		size,
		times['quick'][i],
		times['merge'][i])
