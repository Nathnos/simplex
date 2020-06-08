import math

import numpy as np

from simplex_tools import *

def simplex(A, b, c, z, xB, pivot, show=False):
    #xB makes a feasible solution
    n_iter = 0
    while(np.any(c<-epsilon)):
        n_iter += 1
        r = np.argmin(c) #x_r enter in base
        s = get_s(A, b, r, xB) #x_s leaves the base
        if s is None:
            if show:
                print("Unbounded problem")
            return None, None, np.array([]), math.inf, None, n_iter
        if show:
            print("Interation {} : ".format(n_iter))
            print("Base :", xB)
            print("x{} enters in base, x{} leaves the base".format(r, s))
            print(A)
            print("c = ", c)
            print("b = ", b)
            print("z = ", z)
            print("")
        xB[np.where(xB == s)[0][0]] = r
        A, b, c, z = pivot(xB)
    return A, b, c, z, xB, n_iter
