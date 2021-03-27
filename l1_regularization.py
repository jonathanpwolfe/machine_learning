import numpy as numpy
import matplotlib.pyplot as pyplot

N = 50
D = 50

X = (numpy.random.random((N,D))-0.5)*10

true_w = numpy.array([1,0.5, -0.5] + [0]*(D-3))

Y = X.dot(true_w) +numpy.random.randn(N)*0.5

costs = []

w = numpy.random.randn(D)/ numpy.sqrt(D)
learning_rate = 0.001
l1 = 10

for t in range(500):
	Yhat = X.dot(w)
	delta = Yhat - Y
	w = w - learning_rate*(X.T.dot(delta) +l1*numpy.sign(w))

	mse = delta.dot(delta) / N
	costs.append(mse)

pyplot.plot(costs)
pyplot.show()

print( "final w:" , w)

pyplot.plot(true_w, label = 'true w')
pyplot.plot(w, label = 'w_map')
pyplot.legend()
pyplot.show()