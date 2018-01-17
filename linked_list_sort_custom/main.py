
# Simple node class
class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

# Linked list class (seen in video lesson)
class linked_list:
	def __init__(self):
		self.head=node()

	# Adds new node containing 'data' to the end of the linked list.
	def append(self,data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	# Returns the length (integer) of the linked list.
	def length(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total 

	# Prints out the linked list in traditional Python list format. 
	def display(self):
		elems=[]
		cur_node=self.head
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print elems

	# Returns the value of the node at 'index'. 
	def get(self,index):
		if index>=self.length() or index<0:
			print "ERROR: 'Get' Index out of range!"
			return None
		cur_idx=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: return cur_node.data
			cur_idx+=1

	# Deletes the node at index 'index'.
	def erase(self,index):
		if index>=self.length() or index<0:
			print "ERROR: 'Erase' Index out of range!"
			return 
		cur_idx=0
		cur_node=self.head
		while True:
			last_node=cur_node
			cur_node=cur_node.next
			if cur_idx==index:
				last_node.next=cur_node.next
				return
			cur_idx+=1

	# Allows for bracket operator syntax (i.e. a[0] to return first item).
	def __getitem__(self,index):
		return self.get(index)

	# ADDED THIS METHOD
	# Simplifies the code for selection sort,
	# swaps the values at input indices 'index_1'
	# and 'index_2', all other values unchanged
	def swap(self,index_1,index_2):
		val_1=self.get(index_1) # value at 'index_1'
		val_2=self.get(index_2) # value at 'index_2'

		# Iterate through list and replace values
		cur_idx=0
		cur_node=self.head
		while cur_idx<self.length():
			cur_node=cur_node.next
			if cur_idx==index_1: 
				cur_node.data=val_2
			if cur_idx==index_2:
				cur_node.data=val_1
			cur_idx+=1

# Selection sort tailored to work for a linked list input,
# assuming a linked list with the attributes of the above class
def linked_list_selection_sort(L):
	sort_idx=0 # end of sorted portion of array
	while sort_idx<L.length():
		min_idx=None # to be the index of the next smallest value 
		min_val=None # to be the smallest value found
		# iterate through unsorted portion and find smallest item
		for i in range(sort_idx,L.length()):
			if min_idx==None or L[i].name<min_val:
				min_idx=i
				min_val=L[i].name
		# increase sorted portion by swapping in next smallest
		# item at the righthand side (end of sorted portion)
		L.swap(min_idx,sort_idx)
		sort_idx+=1
	return L

# Create instance of linked list class
arr=linked_list()

# Custom object held in list
class obj:
	def __init__(self,name='none'):
		self.name=name
	def __repr__(self):
		return self.name

# Add some elements in unsorted order
arr.append(obj('z'))
arr.append(obj('y'))
arr.append(obj('x'))
arr.append(obj('w'))

# Display the unsorted list
arr.display()

# Sort using custom selection sort
linked_list_selection_sort(arr)

# Display the (now sorted) list
arr.display()