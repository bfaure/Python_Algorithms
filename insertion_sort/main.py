
# creates randomized arrays for testing
def create_array(size=10,max=50):
	from random import randint
	return [randint(0,max) for _ in range(size)]

# executes insertion sort on the input array 
def insertion_sort(a):
	for sort_len in range(1,len(a)):
		cur_item=a[sort_len] # next item to insert
		insert_idx=sort_len # current index of item
		# iterate down until we reach appropriate insertion location
		while insert_idx>0 and cur_item<a[insert_idx-1]:
			a[insert_idx]=a[insert_idx-1] # shift elements to make room
			insert_idx+=-1 # decrement the insertion index
		a[insert_idx]=cur_item # insert at correct location
	return a


a=create_array()
print a 
a=insertion_sort(a)
print a 