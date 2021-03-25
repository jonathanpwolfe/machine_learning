import numpy as numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as pyplot

#load the data
data_file = None
X = []
Y = []

for line in open ['data_file']:
	x1, x2, y = line.split(',')
	X.append([float(x1), float(x2),1])
	Y.append(float(y))

# turn X and Y into numpy arrays

X = numpy.array(X)
Y = numpy.array(Y)

# plot the data

figure = pyplot.figure()
ax = figure.add_subplot(111, projection='3d')
ax.scatter(X[:,0],X[:,1],Y)
pyplot.show()


#calculate weights

w = numpy.linalg.solve(numpy.dot(X.T,X),numpy.dot(X.T, Y))
Yhat = numpy.dot(X,w)

#compute r-squared

d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print("r-squared: ",r2
)

