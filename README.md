# Simpex Linear Solver
A linear solver in Python using the simplex algorithm.

## Usage
Enter the problem in lauch.py, then execute it.

## Translate the problem

### Cost function
The cost function is cx. That means c are the coefficents of the decision variable.

### Min/Max
If the problem is a maximisation, variable 'isMax' must be True; and False for a minimisation.

### Constraints
Ax ≤ b for standard form.

- The A matrix are the coefficents. One line per constraint. One column per variable.

- The x array represent the decision variables.

- The b array are the right part of the inequations.

### Non-standard constraint
If you have a constraint like cx = b or cx ≥ b, just change the c_type. The n_th number is for the n_th constraint.

- 0 : cx = b

- 1 : cx ≤ b

- -1 : cx ≥ b

If you enter c_type=None, it will be the standard Ax ≤ b for maximisation and Ax ≥ b for minimisation.

### Starting Base
If you know the starting base, write variable's number in an array named 'xB'. It may improve the running time.

### Integer solution
If you need a whole number as a solution, let integer_sol=True. It will trigger a NP alogrithm (very long).

### Show details
Just let full_show=True. Gives the step by step algorithm progression.
