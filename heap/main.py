
class min_heap:
	def __init__(self):
		self.data=[0]
		self.size= 0

	def insert(self,value):
		self.data.append(value)
		self.size+=1
		self._percolate_up(self.size)

	def _percolate_up(self,i):
		while i//2>0:
			if self.data[i]<self.data[i//2]:
				self.data[i],self.data[i//2]=self.data[i//2],self.data[i]
			i=i//2

	def _percolate_down(self,i):
		while (i*2)<=self.size:
			min_child=self._min_child(i)
			if self.data[i]>self.data[min_child]:
				self.data[i],self.data[min_child]=self.data[min_child],self.data[i]
			i=min_child

	def _min_child(self,i):
		if i*2+1>self.size: return i*2
		else:
			if self.data[i*2]<self.data[i*2+1]: return i*2
			else:                               return i*2+1

	def pop_min(self):
		min=self.data[1]
		self.data[1]=self.data[self.size]
		self.size+=-1
		self.data.pop()
		self._percolate_down(1)
		return min

	def 






