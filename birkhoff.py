import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from math import *

MAXN = 10

def next_iterate(f, ts, domain, prev, n):
    fn = []
    for index in range(len(domain)):
        fn.append( (f(ts[index]) + (n-1)*prev[index])/n )
    return fn

def next_ts(t, ts):
    next_t = []
    for i in ts[-1]:
        next_t.append(t(i))
    return next_t


def plot(alpha, f):
    rotation = lambda x: (x + alpha) % 1
    domain = list(np.linspace(0.0, 1.0, 1000))
    F = lambda x: eval(f)
    int_F = integrate.quad(F, 0.0, 1.0)[0]
    plt.plot(domain, [int_F] * len(domain), label='f')
    fns = [[F(x) for x in domain]]
    ts = [domain]
    for n in range(1, MAXN):
        ts.append(next_ts(rotation, ts))
        fns.append(next_iterate(F, ts[n], domain, fns[-1], n))
    #    fns.append(next_iterate(F, rotation, domain, fns[-1], n))
    #fns = [[get_sums(F, rotation, x, n) for x in domain] for n in range(1, MAXN)]
    for index, fn in enumerate(fns):
        plt.plot(domain, fn, label='f'+str(index))
    plt.show()

if __name__ == "__main__":
    alpha = float(input("Enter a rotation value:")) % 1
    f = input("Please enter an L^1 function. (Currently supports polynomials and basic trig functions of 1 variable).")
    plot(alpha, f)
