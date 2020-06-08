import numpy as np

from simplex_tools import *
from simplex import simplex

def find_starting_base(A, b, c, pivot, show):
    xB = np.arange(A.shape[0])
    if(is_solution(xB, A, b)):
        return xB
    if show:
        print("Adding artificial variable, to find initial basis")
    probl_var = problematic_var(xB, A, b)
    nb_probl_var = probl_var.shape[0]
    c2 = np.zeros(c.shape[0] + nb_probl_var) #Objectif is now
    c2[:nb_probl_var] = 1
    A2 = np.zeros((A.shape[0], A.shape[1]+nb_probl_var))
    A2[:, nb_probl_var:] = A
    for i, var in enumerate(probl_var):
        A2[var, i] = 1
    xB = np.zeros(A2.shape[0])
    non_problematic_var = np.delete(np.arange(nb_probl_var, A2.shape[1]),
        probl_var)
    xB[:nb_probl_var] = np.arange(nb_probl_var)
    xB[nb_probl_var:] = non_problematic_var[:A2.shape[0] - nb_probl_var]
    xB = xB.astype("int")
    #Basis: artificial variables and gap variables
    pivot = get_pivot(A2, b, c2, 0)
    A2, b2, c2, z = pivot(xB)
    A2, b2, c2, z, xB, _ = simplex(A2, b, c2, z, xB, pivot, show)
    xB -= nb_probl_var
    if(abs(z) < epsilon):
        return xB
    else:
        if show:
            print("No feasible solutions for the problem !")
        return None
