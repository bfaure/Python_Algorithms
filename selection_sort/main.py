
def create_array(length=10,maxint=50):
	from random import randint
	return [randint(0,maxint) for _ in range(length)]

'''
def selection_sort(arr):
	sort_idx=0 # end of sorted portion of array
	while sort_idx<len(arr):
		min_idx=None # index of smallest item found
		for i,elem in enumerate(arr[sort_idx:]):
			if min_idx==None or elem<arr[min_idx]:
				min_idx=i+sort_idx
		arr[sort_idx],arr[min_idx]=arr[min_idx],arr[sort_idx]
		sort_idx+=1
	return arr 
'''		

def selection_sort(arr):
	sort_idx=0 # end of sorted portion of array
	while sort_idx<len(arr):
		min_idx=arr[sort_idx:].index(min(arr[sort_idx:]))+sort_idx
		arr[sort_idx],arr[min_idx]=arr[min_idx],arr[sort_idx]
		sort_idx+=1
	return arr 

a=create_array()
print a
a=selection_sort(a)
print a