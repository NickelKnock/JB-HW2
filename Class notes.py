import copy

# Original list
original_list = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow_copied_list = original_list.copy()  # or original_list[:] or list(original_list)
shallow_copied_list[0][0] = 'a'

# Deep copy
deep_copied_list = copy.deepcopy(original_list)
deep_copied_list[0][0] = 'b'

# Check the results
print("Original list:", original_list)
print("Shallow copied list:", shallow_copied_list)
print("Deep copied list:", deep_copied_list)

import numpy as np

def solve_system(A, b):
    # Solve the linear system Ax = b for x
    x = np.linalg.solve(A, b)
    return x

def main():
    # System 1
    A1 = np.array([[3, 1, -1],
                   [1, 4, 1],
                   [2, 1, 2]])
    b1 = np.array([2, 12, 10])
    solution1 = solve_system(A1, b1)
    print("Solution for System 1:", solution1)

    # System 2
    A2 = np.array([[1, -10, 2, 4],
                   [3, 1, 4, 12],
                   [9, 2, 3, 4],
                   [-1, 2, 7, 3]])
    b2 = np.array([2, 12, 21, 37])
    solution2 = solve_system(A2, b2)
    print("Solution for System 2:", solution2)

if __name__ == "__main__":
    main()
