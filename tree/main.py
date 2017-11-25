
import sys

class node:
	def __init__(self,value=None):
		self.value=value
		self.parent=None # added this
		self.left_child=None
		self.right_child=None

	# added this
	def __str__(self):
		return "Node with value: %d"%self.value

class binary_tree:
	def __init__(self):
		self.root=None

	def insert(self,value):
		if self.root==None: self.root=node(value)
		else: 			    self._insert(value,self.root)

	def _insert(self,value,cur_node):
		if value<cur_node.value:
			if cur_node.left_child!=None: self._insert(value,cur_node.left_child)
			else: 						  
				cur_node.left_child=node(value)
				cur_node.left_child.parent=cur_node # added this 
		else:
			if cur_node.right_child!=None: self._insert(value,cur_node.right_child)
			else: 						   
				cur_node.right_child=node(value)
				cur_node.right_child.parent=cur_node

	def find(self,value):
		return self._find(value,self.root) if self.root!=None else None

	def _find(self,value,cur_node):
		if value==cur_node.value: 
			return cur_node 
		elif value<cur_node.value and cur_node.left_child!=None: 
			return self._find(value,cur_node.left_child)
		elif value>cur_node.value and cur_node.right_child!=None:
			return self._find(value,cur_node.right_child)

	def print_tree(self):
		if self.root!=None: self._print_tree(self.root)

	def _print_tree(self,cur_node):
		if cur_node!=None:
			self._print_tree(cur_node.left_child)
			print "%d "%cur_node.value
			self._print_tree(cur_node.right_child)

	def depth(self):
		return self._depth(self.root,0) if self.root!=None else 0

	def _depth(self,cur_node,cur_depth):
		if cur_node==None: return cur_depth
		left_depth=self._depth(cur_node.left_child,cur_depth+1)
		right_depth=self._depth(cur_node.right_child,cur_depth+1)
		return max(left_depth,right_depth)

	def display(self):
		print "_"*15
		levels=[]
		cur_nodes=[self.root]
		while True:
			if len(cur_nodes)==0: break
			cur_values=[]
			next_nodes=[]
			for n in cur_nodes:
				if n.value!=None:       cur_values.append(n.value)
				if n.left_child!=None:  next_nodes.append(n.left_child)
				if n.right_child!=None: next_nodes.append(n.right_child)
			levels.append(cur_values)
			cur_nodes=next_nodes
		for i,level in enumerate(levels):
			sys.stdout.write("Level %d:  "%i)
			for n in level:
				sys.stdout.write("%d "%n)
			sys.stdout.write("\n")
		print "_"*15

	# performs breath-first search for value parameter
	def bfs(self,value):
		cur_nodes=[self.root]
		while True:
			next_nodes=[]
			for c in cur_nodes:
				if c.value==value: return True
				if c.left_child!=None:  next_nodes.append(c.left_child)
				if c.right_child!=None: next_nodes.append(c.right_child)
			cur_nodes=next_nodes
			if len(cur_nodes)==0:
				return False

	# performs pre-order depth-first search for value parameter
	def dfs(self,value,cur_node=-1):
		if cur_node==-1:          cur_node=self.root
		if cur_node==None:        return False
		if cur_node.value==value: return True
		in_left  =self.dfs(value,cur_node.left_child)
		in_right =self.dfs(value,cur_node.right_child)
		if in_left or in_right: 
			return True
		else:
			return False

	# deletes the specified input node
	def delete_node(self,node):

		# HELPER FUNCTION
		# returns the node with minimum value in a tree (could be a sub-tree)
		def min_value_node(n):
			current=n 
			while current.left_child!=None:
				current=current.left_child
			return current

		# HELPER FUNCTION
		# returns the number of children for the specified node
		def num_children(n):
			num_children=0
			if n.left_child!=None: num_children+=1
			if n.right_child!=None: num_children+=1
			return num_children

		# get the parent of the node to be deleted
		node_parent=node.parent 

		# get the number of children for the node
		node_children=num_children(node)

		# CASE 1 (node has no children)
		if node_children==0:

			# remove the reference to the node from the parent
			if node_parent.left_child==node:
				node_parent.left_child=None
			else:
				node_parent.right_child=None 

		# CASE 2 (node has a single child)
		elif node_children==1:

			# get the child node
			child=node.left_child if node.left_child!=None else node.right_child

			# put the child node in place of the delete node
			if node_parent.left_child==node: node_parent.left_child=child 
			else: node_parent.right_child=child 

			# set the parent of the new child
			child.parent=node_parent

		# CASE 3 (node has two children)
		else:
			# get the inorder successor of the deleted node
			inorder_successor = min_value_node(node.right_child)
			# copy the inorder successor's content to deleted node
			node.value = inorder_successor.value 
			# delete the inorder successor 
			self.delete_node(inorder_successor)

	# deletes the node in the tree with the specified value
	def delete_value(self,value):
		return self.delete_node(self.find(value))


tree = binary_tree()
tree.insert(3)
tree.insert(4)
tree.insert(0)
tree.insert(-4)
tree.insert(2)
tree.insert(8)

tree.display()






