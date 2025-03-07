# This program returns the Upper Triangular matrix, Lower Triangular matrix and the solution to the system of linear equations,
# using Doolittle's method for LU decomposition.

def lud():
    n = int(raw_input("Enter number of dimensions in coefficient matrix: "))  # Take matrix 'a' elements from user
    print "Enter the elements of coefficient matrix", n, "X", n

    # Initialize matrices a, l, and u
    a = [[0] * n for _ in range(n)]
    l = [[0] * n for _ in range(n)]
    u = [[0] * n for _ in range(n)]

    # Input the elements of matrix 'a' (coefficient matrix)
    for s in range(n):
        for w in range(n):
            a[s][w] = u[s][w] = int(raw_input("Enter a" + str(s + 1) + str(w + 1) + ": "))

    b = [0] * n
    print "Now enter the elements of the constant matrix", n, "X 1"

    # Input the elements of vector 'b' (constant matrix)
    for s in range(n):
        b[s] = int(raw_input("Enter b" + str(s + 1) + ": "))  # Take matrix 'b' elements from user

    # Perform LU decomposition
    for i in range(n):  # Lower triangle matrix
        l[i][i] = 1  # Diagonal elements of L are 1

    for i in range(n):  # Upper triangle matrix and lower triangle
        for j in range(i, n):
            temp = sum(l[i][k] * u[k][j] for k in range(i))
            u[i][j] = a[i][j] - temp
        for j in range(i + 1, n):
            temp = sum(l[j][k] * u[k][i] for k in range(i))
            l[j][i] = (a[j][i] - temp) / u[i][i]

    # Solving LC = b using forward substitution
    c = [0] * n
    for i in range(n):
        temp = sum(l[i][j] * c[j] for j in range(i))
        c[i] = b[i] - temp

    # Solving UX = C using backward substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):  # Start from n-1 to 0
        temp = sum(u[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (c[i] - temp) / u[i][i]

    # Output the results
    print "Lower triangle L:", l
    print "Upper triangle U:", u
    print "The solution is:", x


lud()
