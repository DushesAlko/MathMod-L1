from time import process_time_ns

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math

def showGraph(xk, fk, label, n, color):
    plt.figure(n)
    plt.grid()
    plt.plot(xk, fk, c=color)
    plt.xlabel("X")
    plt.ylabel("F")
    plt.title(label)

#Finding F(x)
def f(t):
    return (t * math.exp(-t**2))
x_nodes = []
y_nodes = []
for i in range(0, 21, 2):
    x = i/10
    qua, quaEps, out = sp.integrate.quad(f, 0, x, limit=30, full_output=1)
    x_nodes.append(x)
    y_nodes.append(qua)

#Making Lagrange polynom and spline
lagrange = sp.interpolate.lagrange(x_nodes, y_nodes)
spline = sp.interpolate.make_interp_spline(x_nodes, y_nodes)

def anF(x):
    return (math.exp(x**2) - 1) / (2*math.exp(x**2))

xk = []
l_k = []
f_k = []
s_k = []
for k in range(1, 10):
    x = (k - 0.5)*0.2
    xk.append(x)
    l_k.append(lagrange(x))
    s_k.append(spline(x))
    f_k.append(anF(x))

#Interpolation graphs
showGraph(xk, l_k, "Lagrange", 1, "green")
showGraph(xk, s_k, "Spline", 2, "blue")
showGraph(xk, f_k, "Analytic", 3, "red")

#Eps graphs
lagrangeEps = []
splineEps = []
for i in range(len(f_k)):
    lagrangeEps.append(abs(f_k[i] - l_k[i]))
    splineEps.append(abs(f_k[i] - s_k[i]))
showGraph(xk, lagrangeEps, "Eps Lagrange", 4, "brown")
showGraph(xk, splineEps, "Eps Spline", 5, "purple")
plt.show()