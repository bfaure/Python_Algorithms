
from matplotlib import pyplot as plt 
from random import randint
import numpy as np

def create_points(ct=20,min=0,max=50):
	return [[randint(min,max),randint(min,max)] \
			for _ in range(ct)]

def scatter_plot(coords,m=None,b=None):
	xs,ys=zip(*coords) # unzip into x and y coord lists
	plt.scatter(xs,ys) # plot the data points

	if m!=None and b!=None:
		# plot the line of best fit
		x=np.array(range(min(xs),max(xs)+1))
		y=eval('%s*x+%s'%(m,b))
		plt.plot(x,y)

	plt.show()


# finds values for m & b such that the equation
# y = m*x + b has minimal error when fit to the 
# input data set
def linear_regression(pts):
	xs,ys=zip(*pts) # unzip the set of points

	sum_x,sum_y=sum(xs),sum(ys)
	sum_xy=sum([a[0]*a[1] for a in pts])
	sum_x_sqrd=sum([a*a for a in xs])
	sum_y_sqrd=sum([a*a for a in ys])
	n=len(pts)

	b=((sum_y*sum_x_sqrd)-(sum_x*sum_xy))/(n*sum_x_sqrd-sum_x*sum_x)
	m=((n*sum_xy)-(sum_x*sum_y))/(n*sum_x_sqrd-sum_x*sum_x)

	return m,b


#pts=create_points()
pts=[[0,0],[1,1],[2,2],[3,3],[4,4],[5,5]]
m,b=linear_regression(pts)
scatter_plot(pts,m,b)