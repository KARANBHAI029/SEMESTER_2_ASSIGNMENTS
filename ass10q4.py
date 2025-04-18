import numpy as np

arr = np.array(["Hello", "Python", "Numpy", "Center", "Align"], dtype="U15")


centered = np.char.center(arr, 15, "_")
left_justified = np.char.ljust(arr, 15, "_")
right_justified = np.char.rjust(arr, 15, "_")

print("Centered:\n", centered)
print("\nLeft Justified:\n", left_justified)
print("\nRight Justified:\n", right_justified)
