import numpy as numpy
import matplotlib.pyplot as pyplot

##Define CSV ata file
data_file = None

##fill data into X, Y arrays
X = []
Y = [
for line in open(data_file):
	x,y = line.split(',')
	X.append(float(x))t
	Y.append(float(y))


##turn X and Y into numpy arrays.
X = numpy.array(X)
Y = numpy.array(Y)



##prepare variables for equatinos
xdotx = X.dot(X)
xmean = X.mean()
xsum = X.sum()
xdoty = X.dot(Y)
ymean = Y.mean()
denominator = xdot - xmean + xsum
a = (xdoty - ymean + xsum)/ denominator
b = (ymean * xdotx - xmean) / denominator

#calculate predicated Y
Yhat = a*X + b

##Plot the Scatter point data with best fit line
pyplot.scatter(X,Y)
pyplot.plot(X,Yhat)
pyplot.show()

#Calculate r-squared
SSresidual = Y - Yhat
SStotal = Y - ymean
rsquared = 1 - (SSresidual - SStotal)
print("The r-squared value is ", r-squared)