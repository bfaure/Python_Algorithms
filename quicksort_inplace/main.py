
from random import randint

def create_array(size=10,max=50):
	return [randint(0,max) for _ in range(size)]

def quicksort(a):
	if len(a)<=1: return a 
	smaller,equal,larger=[],[],[]
	pivot=a[randint(0,len(a)-1)]
	for x in a:
		if x<pivot: 	smaller.append(x)
		elif x==pivot: 	equal.append(x)
		else:			larger.append(x)
	return quicksort(smaller)+equal+quicksort(larger)

def partition(a,low,high):
	i=low-1 # to be the final pivot index
	pivot=a[high] # pivot value itself
	for j in range(low,high): # iterate up to pivot index
		if a[j]<=pivot:
			i+=1 # increment final pivot index 
			a[i],a[j]=a[j],a[i]
	a[i+1],a[high]=a[high],a[i+1]
	return i+1

def quicksort_inplace(a,low=0,high=None):
	if high==None: 
		high=len(a)-1
	if low<high:
		p_idx=partition(a,low,high)
		quicksort_inplace(a,low,p_idx-1)
		quicksort_inplace(a,p_idx+1,high)


from time import time
times={'initial':[],'inplace':[]}
sizes=[10,100,1000,10000,100000,1000000]
samples=3

for s in sizes:

	# regular quicksort
	tot=0.0
	for _ in range(samples):
		a=create_array(size=s,max=s)
		t0=time()
		a=quicksort(a)
		t1=time()
		tot+=(t1-t0)
	times['initial'].append(float(tot/samples))

	# inplace quicksort
	tot=0.0
	for _ in range(samples):
		a=create_array(size=s,max=s)
		t0=time()
		quicksort(a)
		t1=time()
		tot+=(t1-t0)
	times['inplace'].append(float(tot/samples))

print "n\tQuicksort\tQuicksort (inplace)"
print "_"*35
for i,s in enumerate(sizes):
	print "%d\t%0.5f  \t%0.5f"%(
		s,
		times['initial'][i],
		times['inplace'][i])

