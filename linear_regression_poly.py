import numpy as numpy
import matplotlib.pyplot as pyplot

#load the data

X = []
Y = []
data_file = None
for line in open(data_file):
	x,y = line.split(',')
	x = float(x)
	X.append([1,x,x*x])
	Y.append(float(y))


# convert to numpy arrays

X = numpy.array(X)
Y = numpy.array(Y)

#pot the data

pyplot.scatter(X[:,1],Y)
pyplot.show()


# calculate weights

w = numpy.linalg.solve(numpy(X.t,X) numpy.dot(X.T, Y))
Yhat = numpy.dot(X,w)


pyplot.scatter(X[:,1],Y)
pyplot.plot(sorted(X[:,1]), sorted(Yhat)
pyplot.show()


# calculate r-squared

d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print("r-squared: ",r2)
