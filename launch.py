import numpy as np

from simplex_linear_solver import linear_solver

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
#Show only 3 decimals

def main():
    #Exemple entier
    # c = np.array([-5, -8])
    # A = np.array([
    #     [1, 1],
    #     [5, 9]
    # ])
    # b = np.array([6, 45])
    # #-1 : ≤ / 1 : ≥ / 0 : =
    # c_type = np.array([-1, -1])
    # isMax = False

    #Exemple cours grains
    # c = np.array([51, 35, 96])
    # A = np.array([
    #     [2, 3, 7],
    #     [1, 1, 0],
    #     [5, 3, 0],
    #     [0.6, 0.25, 1]
    # ])
    # b = np.array([1250, 250, 900, 232.5])
    # c_type = np.array([1, 1, 1, 1])
    # isMax = False

    #Devoir 2 Recherche OP, question 3.1
    c = np.array([-1, -2, -3, 1])
    A = np.array([
        [1, 2, 3, 0],
        [2, 1, 5, 0],
        [1, 2, 1, 1]
    ])
    b = np.array([15, 20, 20])
    #-1 : ≤ / 1 : ≥ / 0 : =
    c_type = np.array([0, 0, 0])
    isMax = False

    z, c, b, xB, sol, n_iter = linear_solver(A, b, c, c_type, xB=None,
    max=isMax, full_show=False, integer_sol=False)
    #TODO infinité de solutions (segement)
    #TODO non borné? mhh

if __name__ == "__main__":
    main()


    # #Exemple trivial
    # c = np.array([0, 0, 0, -10])
    # A = np.array([
    #     [1, 0, 0, 2],
    #     [0, 1, 0, 3],
    #     [0, 0, 1, 8]
    # ])
    # b = np.array([8, 6, 24]).T
    # isMax = False


    # #Exemple cours vin
    # c = np.array([0, 0, 0, 5, 3])
    # A = np.array([
    #     [1, 0, 0, 1, 0],
    #     [0, 1, 0, 0, 1],
    #     [0, 0, 1, 1, 1]
    # ])
    # b = np.array([50, 60, 80]).T
    # isMax = True
    #
    # #Modification coefficient vin après résolution
    # Delta_c = np.array([0, 0, 0, -1, 1])
    # xB = np.array([1, 3, 4])

    #Exemple variables artificielles
    # c = np.array([1, 2])
    # A = np.array([
    #     [1, 1],
    #     [3, -2],
    #     [-1, 4]
    # ])
    # b = np.array([12, 6, 8])
    # c_type = np.array([-1, 1, 1])
    # isMax = True
