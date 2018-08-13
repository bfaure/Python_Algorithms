def binary_search(a,value):
	if len(a)==0 or (len(a)==1 and a[0]!=value):
		return False

	mid=a[len(a)//2]
	if value==mid: return True 
	if value<mid:  return binary_search(a[:len(a)//2],value)
	if value>mid:  return binary_search(a[len(a)//2+1:],value)


a=[1,2,3,4,5,6,7,8,9]
print(binary_search(a,5))