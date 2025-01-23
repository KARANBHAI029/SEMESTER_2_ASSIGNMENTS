import math

# Function to calculate distance between two 3D points
def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)

# List of 10 3D points (example points, you can input your own)
points = [
    (2, 3, 4),
    (3, 4, 5),
    (5, 6, 7),
    (7, 8, 9),
    (1, 1, 1),
    (4, 5, 6),
    (6, 7, 8),
    (8, 9, 10),
    (10, 11, 12),
    (0, 0, 0)
]

# List to store each point and its nearest neighbor
nearest_neighbors = []

# Find nearest neighbor for each point
for i in range(len(points)):
    min_distance = float('inf')
    nearest_neighbor = None
    for j in range(len(points)):
        if i != j:
            d = distance(points[i], points[j])
            if d < min_distance:
                min_distance = d
                nearest_neighbor = points[j]
    nearest_neighbors.append((points[i], nearest_neighbor))

# Output the list of points with their nearest neighbors
for pair in nearest_neighbors:
    print(f"Point {pair[0]} -> Nearest Neighbor {pair[1]}")
