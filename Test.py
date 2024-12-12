import numpy as np
from scipy.optimize import minimize

# Given matrix A and vector b
A = np.array([[1, 0, 0, -1, 0, 0, 0, 0],
              [0, 0, 1, 0, -1, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, -1, 0],
              [0, 0, 1, -1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, -1, 0],
              [0, 0, 0, 0, 0, 1, 0, -1],
              [0, 1, 0, 0, 0, -1, 0, 0],
              [0, 1, -1, 0, 0, 0, 0, 0],
              [1, -1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, -1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, -1, 1]])
b = np.array([2, 4, 7, 1, 5, 8, 6, 0, -1, -2, -9])

# Define the least squares objective function
def objective(x):
    return np.linalg.norm(A @ x - b)**2

# Define the equality constraints for the first three entries of b
def eq_constraint(x, i):
    return A[i, :] @ x - b[i]

# Define the inequality constraints for the remaining entries of b
def ineq_constraint(x, i):
    return A[i, :] @ x - b[i]  # This will be >= 0 for i >= 4

# Initial guess for x
x0 = np.zeros(A.shape[1])

# Constraints for equality and inequality
constraints = []

# Equality constraints for first three entries
for i in range(3):
    constraints.append({'type': 'eq', 'fun': eq_constraint, 'args': (i,)})

# Inequality constraints for remaining entries
for i in range(3, len(b)):
    constraints.append({'type': 'ineq', 'fun': ineq_constraint, 'args': (i,)})

# Solve the optimization problem
result = minimize(objective, x0, constraints=constraints)

# Output the result
print("Solution: ", result.x)
print("Ax = ", A @ result.x)
print(A @ np.array([4.25, 5.25, 5.25, 2.25, 1.25, -.75, -5.75, -11.75]))

