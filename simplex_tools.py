import numpy as np

epsilon = 1.e-10

def split(A, x):
    return (A.T[x]).T

def get_s(A, b, r, xB): #Which variable should leave the base ?
    a_r = split(A, [r]).T[0]
    valid_id = np.where(a_r > epsilon)[0]
    xHB = np.delete(np.arange(A.shape[1]), xB)
    delete = np.where(valid_id == xHB)
    valid_id = np.delete(valid_id, delete)
    valid_id = np.delete(valid_id, [r])
    if valid_id.size == 0:
        return None
    return xB[valid_id[np.argmin(b[valid_id]/a_r[valid_id])]]

def z(A, c, xB):
    return np.sum(split(c*A, xB))

def get_pivot(A, b, c, z):
    def pivot(xB):
        B = split(A, xB)
        cB = split(c, xB)
        B_inv = np.linalg.inv(B)
        A2 = B_inv.dot(A)
        b2 = B_inv.dot(b)
        PI = cB.dot(B_inv)
        c2 = c - PI.dot(A)
        z2 = z - PI.dot(b)
        return A2, b2, c2, z2
    return pivot

def is_solution(xB, A, b):
    B = split(A, xB)
    B_inv = np.linalg.inv(B)
    b = B_inv.dot(b)
    return np.all(b>-epsilon)

def problematic_var(xB, A, b):
    B = split(A, xB)
    B_inv = np.linalg.inv(B)
    b = B_inv.dot(b)
    return np.where(b<epsilon)[0]


#Showing :
def show_result(xB, b):
    for n, i in enumerate(xB):
        print("x{} = {}".format(i, b[n]))

def make_solution(b, xB, maxLength):
    X = np.empty(maxLength)
    for i in range(maxLength):
        if i in xB:
            X[i] = b[np.where(xB==i)]
        else:
            X[i] = 0
    return X


def is_int(sol):
    if sol is None:
        return False
    return np.allclose(sol, np.round(sol))

def add_constraint(A, b, xi, i, sup=False):
    x, y = A.shape
    A2 = np.zeros((x+1, y))
    A2[:-1, :] = A
    b2 = np.zeros(x+1)
    b2[:-1] = b
    b2[-1] = xi
    if sup:
        A2[x, i] = -1
    else:
        A2[x, i] = 1
    return A2, b2

def transform(A, c, c_type):
    n = np.count_nonzero(c_type)
    A2 = np.zeros((A.shape[0], A.shape[1] + n))
    A2[:, n:] = A
    col = 0
    for i in range(A.shape[0]):
        if c_type[i] != 0:
            A2[i, col] = -c_type[i]
            col += 1
    c2 = np.zeros(c.shape[0] + n)
    c2[n:] = c
    return A2, c2
