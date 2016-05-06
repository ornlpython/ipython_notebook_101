#trapSerial.py
#example to run: python trapSerial.py 0.0 1.0 10000

import numpy
import sys
import timeit

start = timeit.default_timer()

#takes in command-line arguments [a,b,n]
a = float(sys.argv[1])
b = float(sys.argv[2])
n = int(sys.argv[3])

def f(x):
        return x*x

def integrateRange(a, b, n):
        '''Numerically integrate with the trapezoid rule on the interval from
        a to b with n trapezoids.
        '''
        integral = -(f(a) + f(b))/2.0
        # n+1 endpoints, but n trapazoids
        for x in numpy.linspace(a,b,n+1):
                integral = integral + f(x)
        integral = integral* (b-a)/n
        return integral

integral = integrateRange(a, b, n)
print("With n =", n, "trapezoids, our estimate of the integral from", a, "to", b, "is", integral)

stop = timeit.default_timer()

print("Running time %r" %(stop-start))

#(py3)mac102217:MPI j35$ python trapSerial.py 0.0 1.0 10000000
#With n = 10000000 trapezoids, our estimate of the integral from 0.0 to 1.0 is 0.333333333333
#Running time 2.7556346580095123
