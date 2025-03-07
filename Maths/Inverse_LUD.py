# Purpose: LU decomposition + find matrix inverse
# Done to find the inverse by solving LC = b and UX = C
# This program solves multiple systems for each column of identity matrix, instead of finding the solution for a single system Ax = b.

def inverse_LUD(n):
    # Initialize matrices
    a = [[0] * n for _ in range(n)]
    l = [[0] * n for _ in range(n)]
    u = [[0] * n for _ in range(n)]
    inv = [[0] * n for _ in range(n)]
    idm = [[0] * n for _ in range(n)]  # Identity matrix
    b = [0] * n

    # Initialize L and U, identity matrix
    for i in range(n):
        for j in range(n):
            if j == i:
                l[i][j] = 1
                idm[i][j] = 1
            else:
                l[i][j] = 0
                idm[i][j] = 0
            u[i][j] = 0
            inv[i][j] = 0

    # Input matrix 'a'
    print "Enter the elements of the matrix whose inverse you want to find out"
    for i in range(n):
        for j in range(n):
            a[i][j] = float(raw_input("a" + str(i + 1) + str(j + 1) + ": "))

    # LU Decomposition
    for i in range(n):  # Lower triangle
        for j in range(i, n):
            temp = 0
            for t in range(i):
                temp += l[i][t] * u[t][j]
            u[i][j] = (a[i][j] - temp) / l[i][i]

        for j in range(i + 1, n):  # Upper triangle
            temp = 0
            for t in range(i):
                temp += l[j][t] * u[t][i]
            l[j][i] = (a[j][i] - temp) / u[i][i]

    # Solving LC = b using forward substitution
    for q in range(n):
        for z in range(n):
            b[z] = idm[z][q]
        
        c = [0] * n
        for i in range(n):
            temp = 0
            for j in range(i):
                temp += l[i][j] * c[j]
            c[i] = b[i] - temp

        # Solving UX = C using backward substitution
        x = [0] * n
        for i in range(n - 1, -1, -1):  # Start from n-1 to 0
            temp = 0
            for j in range(i + 1, n):
                temp += u[i][j] * x[j]
            x[i] = (c[i] - temp) / u[i][i]

        for z in range(n):
            inv[z][q] = x[z]

    # Print the inverse matrix
    print "Inverse matrix:"
    for i in range(n):
        print "   ".join(str(inv[i][j]) for j in range(n))


# Example: Call the function with a 3x3 matrix
n = int(raw_input("Enter the size of the matrix: "))
inverse_LUD(n)
