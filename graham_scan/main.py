
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

# Sorts in order of increasing polar angle from 'anchor' point.
# 'anchor' variable is assumed to be global, set from within 'graham_scan'
def quicksort(a):
	if len(a)<=1: return a 
	smaller,equal,larger=[],[],[]
	piv=a[randint(0,len(a)-1)] # select random pivot
	piv_ang=polar_angle(anchor,piv) # calculate pivot angle
	for pt in a:
		pt_ang=polar_angle(anchor,pt) # calculate current pt angle
		if pt_ang<piv_ang: 		smaller.append(pt)
		elif pt_ang==piv_ang: 	equal.append(pt)
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

		elif determinant(hull[-2],hull[-1],s)==0: # collinear
			hull.append(s)

		else: # clockwise
			while determinant(hull[-2],hull[-1],s)<=0:
				del hull[-1]
				if len(hull)<2: break
			hull.append(s)
		if show_progress: scatter_plot(points,hull)
	return hull 

#pts=[[36, 14], [29, 46], [31, 1], [25, 1], [10, 50], [9, 37], [27, 31], [46, 4], [0, 41], [44, 43], [20, 46], [16, 2], [42, 5], [20, 9], [40, 34], [46, 29], [9, 35], [30, 41], [21, 9], [9, 30], [44, 36], [29, 31], [31, 45], [13, 19], [27, 14], [22, 13], [48, 17], [6, 5], [48, 35], [6, 8], [7, 43], [3, 43], [2, 7], [50, 37], [30, 40], [14, 0], [48, 1], [18, 6], [39, 38], [31, 13], [12, 19], [35, 35], [24, 1], [31, 48], [25, 21], [3, 31], [28, 25], [39, 32], [34, 30], [23, 11], [31, 9], [40, 17], [8, 24], [1, 48], [11, 23], [42, 42], [22, 21], [45, 7], [18, 28], [39, 24], [45, 15], [22, 12], [41, 7], [3, 43], [8, 22], [28, 44], [50, 29], [25, 7], [31, 11], [35, 24], [18, 43], [7, 7], [41, 5], [19, 48], [46, 36], [48, 16], [17, 34], [19, 35], [29, 12], [3, 14], [0, 14], [2, 2], [3, 43], [2, 7], [13, 30], [35, 44], [18, 33], [4, 4], [33, 0], [46, 5], [37, 49], [25, 0], [40, 31], [9, 46], [3, 8], [3, 18], [0, 38], [42, 14], [27, 2], [0, 1], [25, 48], [25, 36], [13, 49], [27, 4], [17, 4], [24, 32], [41, 48], [45, 47], [30, 26], [36, 50], [28, 13], [27, 3], [28, 15], [34, 23], [9, 25], [14, 28], [35, 44], [38, 30], [48, 45], [40, 48], [24, 50], [13, 17], [18, 28], [38, 27], [31, 1], [0, 25], [41, 18], [45, 14], [34, 19], [42, 43], [28, 48], [11, 24], [21, 28], [34, 36], [21, 17], [5, 18], [5, 49], [14, 36], [42, 25], [16, 36], [46, 37], [32, 27], [1, 23], [11, 33], [40, 31], [28, 49], [48, 39], [1, 27], [39, 16], [29, 41], [17, 32], [13, 24], [29, 16], [41, 44], [39, 45], [8, 36], [15, 1], [38, 27], [24, 47], [10, 42], [5, 20], [32, 42], [33, 30], [22, 47], [31, 18], [40, 49], [43, 30], [19, 10], [36, 10], [21, 13], [26, 27], [37, 31], [38, 39], [20, 15], [28, 30], [44, 10], [26, 0], [7, 41], [42, 25], [4, 32], [32, 31], [32, 4], [26, 2], [48, 43], [10, 36], [21, 17], [42, 28], [45, 44], [40, 48], [41, 26], [5, 14], [9, 3], [7, 8], [40, 15], [0, 7], [1, 22], [42, 49], [17, 37], [31, 50], [47, 17], [40, 42], [37, 0], [1, 1], [40, 29], [16, 38], [27, 49], [28, 6], [37, 38], [18, 7], [46, 27], [18, 2], [1, 46], [50, 1], [41, 20], [35, 13], [42, 41], [12, 0], [5, 34], [4, 44], [23, 38], [36, 40], [30, 45], [32, 34], [13, 27], [31, 50], [15, 43], [15, 4], [13, 38], [25, 26], [12, 27], [40, 0], [5, 26], [9, 27], [29, 8], [49, 32], [5, 24], [49, 48], [48, 46], [42, 46], [7, 43], [46, 31], [45, 11], [48, 0], [33, 16], [41, 30], [5, 7], [24, 13], [18, 8], [10, 17], [31, 17], [9, 24], [17, 48], [8, 18], [45, 11], [25, 12], [46, 2], [32, 36], [33, 15], [0, 20], [8, 37], [0, 2], [43, 9], [38, 11], [11, 40], [13, 45], [13, 40], [12, 11], [50, 46], [22, 38], [12, 25], [14, 49], [33, 31], [40, 39], [30, 43], [35, 41], [9, 46], [35, 34], [15, 5], [40, 14], [3, 27], [29, 43], [24, 42], [29, 40], [16, 23], [9, 43], [37, 35], [2, 48], [1, 40], [35, 27], [17, 6], [17, 11], [36, 38], [0, 5], [29, 21], [32, 31], [50, 39], [14, 18], [38, 6], [41, 12], [17, 34], [8, 7], [18, 36], [15, 13], [8, 1], [47, 28], [33, 9], [29, 26], [6, 20], [33, 7], [5, 45], [23, 36], [49, 40], [9, 26], [14, 43], [25, 28], [9, 24], [5, 48], [22, 37], [30, 21], [27, 27], [48, 12], [43, 15], [27, 39], [11, 4], [41, 32], [50, 14], [22, 14], [6, 21], [18, 48], [39, 7], [36, 12], [40, 7], [10, 45], [46, 32], [44, 44], [38, 32], [40, 41], [47, 2], [31, 44], [10, 45], [19, 39], [42, 20], [7, 5], [10, 23], [36, 46], [16, 36], [22, 31], [27, 20], [50, 42], [7, 28], [19, 50], [15, 29], [22, 9], [20, 24], [42, 0], [24, 25], [38, 0], [42, 32], [13, 16], [33, 13], [8, 43], [37, 10], [18, 22], [11, 24], [31, 9], [6, 25], [15, 49], [13, 36], [1, 4], [13, 42], [12, 36], [49, 26], [34, 8], [41, 39], [48, 37], [13, 10], [11, 47], [39, 4], [4, 7], [9, 42], [49, 2], [37, 29], [34, 22], [11, 9], [21, 43], [22, 0], [40, 25], [47, 41], [2, 24], [3, 24], [41, 10], [48, 32], [50, 7], [15, 17], [38, 38], [37, 35], [11, 26], [31, 25], [25, 28], [22, 26], [28, 18], [8, 14], [17, 15], [14, 14], [33, 43], [25, 36], [15, 34], [20, 1], [24, 37], [33, 24], [42, 28], [22, 27], [8, 18], [9, 5], [8, 20], [15, 26], [28, 3], [28, 19], [41, 33], [43, 29], [4, 15], [13, 15], [7, 43], [38, 44], [39, 33], [22, 37], [22, 44], [35, 45], [24, 36], [15, 29], [16, 37], [17, 9], [8, 42], [12, 24], [45, 31], [5, 25], [40, 38], [29, 42], [0, 26], [16, 31], [4, 30], [24, 40], [9, 28], [20, 4], [37, 1], [25, 42], [18, 6], [26, 36], [31, 31], [2, 41], [9, 8], [14, 42], [47, 19], [44, 28], [38, 18], [31, 22], [0, 2], [44, 7], [2, 12], [0, 41], [39, 14], [38, 27], [7, 34], [28, 44], [1, 34], [37, 34], [38, 19], [0, 46], [12, 13], [12, 40], [8, 33], [29, 46], [14, 34], [49, 23], [4, 46], [21, 38], [10, 36], [1, 4], [39, 30], [16, 17], [43, 16], [46, 42], [35, 2], [49, 46], [8, 37], [5, 40], [39, 11], [8, 15], [49, 42], [46, 23], [17, 25], [27, 1], [47, 2], [33, 28], [33, 18], [40, 17], [35, 15], [14, 33], [33, 17], [21, 2]]
#pts = [[6, 3], [18, 2], [14, 9], [10, 14], [16, 20], [15, 18], [1, 15], [2, 1], [13, 3], [19, 7], [1, 1], [2, 5], [3, 19], [7, 15], [14, 20], [8, 6], [8, 17], [17, 11], [14, 11], [11, 0], [5, 15], [5, 1], [16, 1], [14, 12], [8, 12], [17, 0], [6, 17], [3, 17], [8, 0], [6, 18], [14, 10], [7, 2], [14, 19], [16, 6], [15, 7], [1, 10], [9, 9], [5, 9], [5, 1], [13, 17], [13, 13], [4, 14], [0, 20], [13, 10], [8, 12], [13, 0], [3, 17], [0, 13], [15, 3], [14, 10]]
#pts=[[5, 4], [3, 5], [3, 4], [2, 2], [0, 1], [0, 4], [0, 3], [5, 2], [1, 2], [4, 2], [0, 4], [4, 1], [1, 5], [4, 3], [3, 3], [0, 1], [3, 0], [1, 2], [5, 3], [4, 2]]

#pts = [[1,1],[5,1],[5,5],[1,5],[3,1]]

pts=create_points(500,0,50)
print "points:",pts
hull=graham_scan(pts,False)
print "hull:",hull
scatter_plot(pts,hull)