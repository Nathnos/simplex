"""
Algo du simplexe, en minimisation par défaut
"""

import math

import numpy as np

from simplex.starting_base import find_starting_base, is_solution
from simplex.tools import *
from simplex.simplex_algo import simplex

def linear_solver(A, b, c, c_type, xB=None, max=True, z=0, integer_sol=False,
    show=True, full_show=False):
    """
    Do all the preprocessing stuff for simplex algorithms
    """
    nb_var = A.shape[1]
    if c_type is None:
        nb_constraints = A.shape[0]
        if max:
            c_type = [-1 for _ in range(nb_constraints)]
        else:
            c_type = [1 for _ in range(nb_constraints)]
    A, c = transform(A, c, c_type)
    if max:
        c = -c
    if integer_sol:
        _, _, b, xB, sol, n_iter, z = integer_solutions(A, b, c, xB, max, z,
            show, full_show, None, 0, nb_var, math.inf)
        sol = np.round(sol).astype("int")
    else:
        z, _, b, xB, sol, n_iter = floating_solutions(A, b, c, xB, max, z,
            show, full_show)
    if show or full_show:
        print(sol[-nb_var:], z if max else -z)
    if max:
        return z, -c, b, xB, sol, n_iter
    return -z, c, b, xB, sol, n_iter

def floating_solutions(A, b, c, xB, max, z, show, full_show):
    """
    Classic simplex
    """
    pivot = get_pivot(A, b, c, z) #Closure with initial values
    if xB is None or not is_solution(xB, A, b, c):
        xB = find_starting_base(A, b, c, pivot, full_show)
    if xB is None:
        return math.inf, np.array([]), None, None, np.array([]), 0
    A, b, c, z = pivot(xB) #Go to base xB
    A, b, c, z, xB, n_iter = simplex(A, b, c, z, xB, pivot, full_show)
    if A is not None:
        sol = make_solution(b, xB, A.shape[1])
    else:
        sol = np.array([])
    return z, c, b, xB, sol, n_iter

def integer_solutions(A, b, c, xB, max, z_init, show, full_show, sol, n_iter,
    nb_var, minimal_z):
    """
    Integer solutions only, branch and bound
    """
    z, c2, b2, xB, sol, iter = floating_solutions(A, b, c, None, max, z_init,
        full_show, full_show)
    n_iter += iter
    if xB is not None and not is_int(sol[-nb_var:]) and z < minimal_z:
        var_sol = sol[-nb_var:]
        x = np.argmax(np.ceil(var_sol) != np.floor(var_sol))
        x += sol.shape[0] - nb_var
        x1 = int(np.floor(sol[x]))
        x2 = int(np.ceil(sol[x]))
        A1, b1 = add_constraint(A, b, x1, x, sup=False)
        A2, b2 = add_constraint(A, b, x2, x, sup=True)
        z1, c1, b1, xB1, sol1, iter1, minimal_z1 = integer_solutions(A1, b1, c,
            xB, max, z_init, show, full_show, sol, n_iter, nb_var, minimal_z)
        z2, c2, b2, xB2, sol2, iter2, minimal_z2 = integer_solutions(A2, b2, c,
            xB, max, z_init, show, full_show, sol, n_iter, nb_var, minimal_z)
        minimal_z = min(minimal_z, minimal_z1, minimal_z2)
        n_iter += iter1 + iter2
        if z1 < z2: #if True, z1 can't be infinite
            return z1, c1, b1, xB1, sol1, n_iter, minimal_z
        if xB2 is None:
            return (math.inf, np.array([]), None, None, np.array([]),
                0, minimal_z)
        return z2, c2, b2, xB2, sol2, n_iter
    else: #End of branching, solution found
        minimal_z = min(minimal_z, z)
        return z, c2, b2, xB, sol, iter, minimal_z
