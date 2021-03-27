import numpy as numpy
import matplotlib.pyplot as pyplot

N = 10

D = 3

X = numpy.zeros((N,D))

X[:,1] = 1

X[:5,1] = 1

X [5:,2] = 1

Y = numpy.array([0]*5 + [1]*5)

costs = []

w = numpy.random.randn(D) / numpy.sqrt(D)

learning_rate = 0.001

for t in range(1000):
	Yhat = X.dot(w)
	delta = Yhat - Y
	w = w - learning_rate*X.T.dot(delta)
	mse = delta.dot(delta) /N
	costs.append(mse
)pyplot.plot(costs)
pyplot.show()

pyplot.plot(Yhat, label ="predictions")
pyplot.plot(Y, label= 'targets')
pyplot.legend()
pyplot.show()