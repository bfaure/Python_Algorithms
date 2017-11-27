
from matplotlib import pyplot as plt # for plotting
import numpy as np # for plotting
from random import randint # for creating data points
from math import atan2 # for computing polar angle

# Creates a scatter plot, input is a list of (x,y) coordinates.
# The second input 'convex_hull' is another list of (x,y) coordinates
# consisting of those points in 'coords' which make up the convex hull,
# if not None, the elements of this list will be used to draw the outer
# boundary (the convex hull surrounding the data points).
def scatter_plot(coords,convex_hull=None):
	xs=[pt[0] for pt in coords] # x coordinates
	ys=[pt[1] for pt in coords] # y coordinates

	xs,ys=np.array(xs),np.array(ys) # convert to numpy arrays
	plt.scatter(xs,ys) # plot the data points

	if convex_hull!=None:
		# plot the convex hull boundary
		for i in range(1,len(convex_hull)):
			c0=convex_hull[i-1]
			c1=convex_hull[i]
			plt.plot((c0[0],c1[0]),(c0[1],c1[1]),'r')
		first=convex_hull[0]
		last=convex_hull[-1]
		plt.plot((last[0],first[0]),(last[1],first[1]),'r')
	plt.show() # show the plot

# Returns a list of unique (x,y) coordinates of length 'num_points',
# each x and y coordinate is chosen randomly from the range 
# 'min' up to 'max'.
def create_points(num_points,min=0,max=50):
	pts=[]
	for _ in range(num_points):
		while True:
			x,y=randint(min,max),randint(min,max)
			if [x,y] not in pts:
				pts.append([x,y])
				break
	return pts

# Returns the polar angle (radians) from p0 to p1.
# p0 is assumed to be the point with the lowest y coordinate.
def polar_angle(p0,p1):
	y_span=p1[1]-p0[1]
	x_span=p1[0]-p0[0]
	return atan2(y_span,x_span)

# Returns the euclidean distance from p0 to p1,
# square root is not applied for sake of speed
def distance(p0,p1):
	y_span=p1[1]-p0[1]
	x_span=p1[0]-p0[0]
	return y_span**2+x_span**2

# Sorts in order of increasing polar angle from 'anchor' point.
# 'anchor' variable is assumed to be global, set from within 'graham_scan'.
# For any values with equal polar angles, a second sort is applied to
# ensure increasing distance from the 'anchor' point.
def quicksort(a):
	if len(a)<=1: return a 
	smaller,equal,larger=[],[],[]
	piv=a[randint(0,len(a)-1)] # select random pivot
	piv_ang=polar_angle(anchor,piv) # calculate pivot angle
	for pt in a:
		pt_ang=polar_angle(anchor,pt) # calculate current pt angle
		if pt_ang<piv_ang: 		smaller.append(pt)
		elif pt_ang==piv_ang:
			# if polar angle is the same, sort by increasing distance
			equal.append(pt)
			temp=[]
			while len(equal)>0:
				min_dist,min_idx=None,None
				for i,e in enumerate(equal):
					if min_dist==None or distance(e,anchor)<min_dist:
						min_dist=distance(e,anchor)
						min_idx=i 
				temp.append(equal[min_idx])
				del equal[min_idx]
			equal=temp
		else:					larger.append(pt)
	return quicksort(smaller)+equal+quicksort(larger)

# Returns the determinant of the 3x3 matrix...
# 	[p1(x) p1(y) 1]
#	[p2(x) p2(y) 1]
# 	[p3(x) p3(y) 1]
# If >0 then counter-clockwise
# If <0 then clockwise
# If =0 then collinear
def determinant(p1,p2,p3):
	return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

# Returns the vertices comprising the boundaries of
# convex hull containing all points in the input set. 
# The input 'points' is a list of (x,y) coordinates.
# If 'show_progress' is set to True, the progress in 
# constructing the hull will be plotted on each iteration.
def graham_scan(points,show_progress=False):	
	global anchor # to be set, (x,y) with smallest y value

	# Find the (x,y) point with the lowest y value,
	# along with its index in the 'points' list. If
	# there are multiple points with the same y value,
	# choose the one with smallest x.
	min_y,min_idx=None,None
	for i,(x,y) in enumerate(points):
		if min_y==None or y<min_y:
			min_y,min_idx=y,i 
		if y==min_y and x<points[min_idx][0]:
			min_idx=i
	anchor=points[min_idx] # pt with min y value

	sorted_pts=points[:] # make copy of input points
	del sorted_pts[min_idx] # remove anchor point
	sorted_pts=quicksort(sorted_pts) # sort the points by polar angle

	# anchor and point with smallest polar angle will always be on hull
	hull=[anchor,sorted_pts[0]] 

	# iterate over points in increasing polar angle
	for s in sorted_pts[1:]:
		if determinant(hull[-2],hull[-1],s)>0: # counter clockwise
			hull.append(s)
		else: # clockwise
			while determinant(hull[-2],hull[-1],s)<=0:
				del hull[-1]
				if len(hull)<2: break
			hull.append(s)
		if show_progress: scatter_plot(points,hull)
	return hull 

pts=create_points(500,0,50)
print "points:",pts
hull=graham_scan(pts,False)
print "hull:",hull
scatter_plot(pts,hull)