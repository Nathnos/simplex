import numpy as np

from simplex.linear_solver import linear_solver

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
#Show only 3 decimals

def main():
    c = np.array([51, 35, 96])
    A = np.array([
        [2, 3, 7],
        [1, 1, 0],
        [5, 3, 0],
        [0.6, 0.25, 1]
    ])
    b = np.array([1250, 250, 900, 232.5])
    #-1 : ≤ / 1 : ≥ / 0 : =
    c_type = np.array([1, 1, 1, 1])
    isMax = False

    z, c, b, xB, sol, n_iter = linear_solver(A, b, c, c_type=None, xB=None,
    max=isMax, full_show=False, integer_sol=False)

if __name__ == "__main__":
    main()
