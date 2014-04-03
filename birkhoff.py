import matplotlib.pyplot as plt
import numpy as np
from math import *

MAXN = 1000

#def rotation(x, alpha):
#    """
#    Defines a circle rotation by alpha.
#    
#    @param x the point being rotated
#    @param alpha the angle to rotate by.
#    """
#    return (x + alpha) % 1
def get_sums(f, t, x):
    ns = [f(x)]
    ts = [x]
    for n in range(1,MAXN):
        ts.append(t(ts[n-1]))
        ns.append(ns[n-1] + f(ts[n]))
        ns[n-1] = ns[n-1]/(n) #Divide by n because indices don't line up
    return ns

def plot(alpha, f):
    rotation = lambda x: (x + alpha) % 1
    domain = list(np.linspace(0.0, 1.0, 1000))
    F = lambda x: eval(f)
    fns = [[g for g in get_sums(F, rotation, x)] for x in domain]
    for fn in fns:
        plt.plot(domain, fn)
    #image = [(x + alpha) % 0 for x in domain]
    #plt.plot(domain, image)
    #plt.show()

if __name__ == "__main__":
    alpha = float(input("Enter a rotation value:"))
    f = input("Please enter an L^1 function. (Currently supports polynomials of 1 variable).")
    plot(alpha, f)
