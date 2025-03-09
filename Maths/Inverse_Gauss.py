# Compute inverse matrix via Gauss elimination

def Gauss():

    n = int(raw_input("Enter number of dimensions in the square matrix: "))
    print("Enter the elements of the matrix", n, "X", n)
    
    # Read the coefficient matrix
    x = [[0] * n for _ in range(n)]
    for s in range(0, n):
        for w in range(0, n):
            x[s][w] = int(raw_input(f"Enter x{s+1}{w+1}: "))

    # Create an identity matrix for the augmented matrix
    identity = [[0 if i != j else 1 for j in range(n)] for i in range(n)]
    
    # Augment the original matrix with the identity matrix
    augmented_matrix = [x[i] + identity[i] for i in range(n)]
    
    # Perform Gaussian elimination to transform the matrix into row echelon form
    for s in range(0, n):
        # Make the diagonal element 1 by dividing the entire row by the diagonal element
        pivot = augmented_matrix[s][s]
        if pivot == 0:
            print("The matrix is singular and cannot be inverted.")
            return
        for w in range(0, 2*n):
            augmented_matrix[s][w] /= pivot
        
        # Eliminate the elements below the pivot
        for w in range(s + 1, n):
            factor = augmented_matrix[w][s]
            for q in range(s, 2*n):
                augmented_matrix[w][q] -= factor * augmented_matrix[s][q]

    # Back-substitution to eliminate elements above the pivot
    for s in range(n - 1, -1, -1):
        for w in range(s - 1, -1, -1):
            factor = augmented_matrix[w][s]
            for q in range(s, 2*n):
                augmented_matrix[w][q] -= factor * augmented_matrix[s][q]
    
    # Extract the inverse from the augmented matrix (the right half of the augmented matrix)
    inverse_matrix = [row[n:] for row in augmented_matrix]
    
    # Print the inverse matrix
    print("The inverse matrix is:")
    for row in inverse_matrix:
        print(row)

Gauss()
