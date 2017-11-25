
# recursive implementation of function, prints out the
# first n fibonacci numbers
def fibonacci(n,cur_fib=[1,1],i=0):
	if i==n:
		return
	if i<2:
		print cur_fib[i]
		return fibonacci(n,cur_fib,i+1)
	else:
		new_fib=sum(cur_fib)
		print new_fib
		return fibonacci(n,[cur_fib[1],new_fib],i+1)

fibonacci(8)

