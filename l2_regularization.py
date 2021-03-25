import numpy as numpy
import matplotlib.pyplot as pyplot

# set number of data points to 50 evenely spaced points between 0 and 10
N = 50
X = numpy.linspace(0,10,N)

# make Y .5 * X with random noise
Y = 0.5*X + numpy.random.randn(N)

#make last two points 30 larger than they are
Y[-1] += 30
Y[-2] +=30

#plot the points
pyplot.scatter(X,Y)
pyplot.show()

#add bias term
X = numpy.vstack([numpy.ones(N), X]).T

# calculate maximum likelihood solution and plot it.
w_ml = numpy.linalg.solve(X.T.dot(X), X.T.dot(Y))
Yhat_ml = X.dot(w_ml)
pyplot.scatter(X[:,1],Y)
pyplot.scatter(X[:,1], Yhat_ml)
pyplot.show()

#l2 count to 1000
l2 = 1000.0

# set to forumula for l2
w_map = numpy.linalg.solve(l2*numpy.eye(2) + X.T.dot(X), X.T.dot(Y))
Yhat_map = X.dot(w_map)

# plot the data
pyplot.scatter(X[:,1], Y)
pyplot.scatter(X[:,1], Yhat_ml, label= "maximim likelihood")
pyplot.scatter(X[:,1], Yhat_map, label = "map")
pyplot.legend()
pyplot.show()
