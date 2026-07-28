# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def input_matrix(rows, cols, label=""):
    """Reads a matrix from user input row by row."""
    if label:
        print(f"\nEntering Matrix {label}:")
    matrix = []
    for i in range(rows):
        row_str = input(f"Enter row {i + 1}: ")
        row = [int(val) for val in row_str.strip().split()]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    """Prints a matrix formatted in aligned columns."""
    for row in matrix:
        for val in row:
            print(f"{val:<4}", end="")
        print()


def transpose(matrix):
    """Computes the transpose of an M x N matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
        
    return transposed


def add_matrices(a, b):
    """Computes element-wise sum of two M x N matrices using nested loops."""
    rows = len(a)
    cols = len(a[0])
    result = []
    
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(a[i][j] + b[i][j])
        result.append(row)
        
    return result


def multiply_matrices(a, b):
    """Computes matrix product of A (M x N) and B (N x P) using nested loops."""
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            cell_sum = 0
            for k in range(cols_a):
                cell_sum += a[i][k] * b[k][j]
            row.append(cell_sum)
        result.append(row)
        
    return result


def main():
    # --- PART A: TRANSPOSE ---
    print("--- PART A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix_a = input_matrix(rows, cols)

    print("\nOriginal Matrix:")
    print_matrix(matrix_a)

    transposed_a = transpose(matrix_a)
    print("\nTransposed Matrix:")
    print_matrix(transposed_a)

    # --- PART B: ADDITION ---
    print("\n--- PART B: Add Two Matrices ---")
    rows_b = int(input("Enter number of rows for both matrices: "))
    cols_b = int(input("Enter number of columns for both matrices: "))

    mat1 = input_matrix(rows_b, cols_b, "1")
    mat2 = input_matrix(rows_b, cols_b, "2")

    sum_res = add_matrices(mat1, mat2)
    print("\nSum Matrix:")
    print_matrix(sum_res)

    # --- PART C: MULTIPLICATION ---
    print("\n--- PART C: Multiply Two Matrices ---")
    rows1 = int(input("Enter Matrix A rows: "))
    cols1 = int(input("Enter Matrix A columns (and Matrix B rows): "))
    cols2 = int(input("Enter Matrix B columns: "))

    mat_a = input_matrix(rows1, cols1, "A")
    mat_b = input_matrix(cols1, cols2, "B")

    mult_res = multiply_matrices(mat_a, mat_b)
    print("\nProduct Matrix (A x B):")
    print_matrix(mult_res)


if _name_ == "_main_":
    main()