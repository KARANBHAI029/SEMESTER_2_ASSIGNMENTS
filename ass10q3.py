import numpy as np

N = 10  
cartesian_points = np.random.rand(N, 2) * 20 


r = np.sqrt(cartesian_points[:, 0]**2 + cartesian_points[:, 1]**2)
theta = np.arctan2(cartesian_points[:, 1], cartesian_points[:, 0])

polar_points = np.column_stack((r, theta))

print("Cartesian Points:\n", cartesian_points)
print("\nPolar Coordinates:\n", polar_points)
