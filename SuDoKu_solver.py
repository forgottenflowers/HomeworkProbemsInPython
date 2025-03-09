# Take the SuDoKu puzzle as a grid input and solve it

def print_grid(grid):
    """Prints the Sudoku grid in a readable format."""
    for row in grid:
        print " ".join(str(x) if x != 0 else "." for x in row)


def is_valid(grid, row, col, num):
    """Checks if num can be placed in grid[row][col]."""
    
    # Check row
    if num in grid[row]:
        return False
    
    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check 3x3 subgrid
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(grid):
    """Solves the Sudoku using backtracking."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Find empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        
                        if solve_sudoku(grid):  # Recursive step
                            return True
                        
                        grid[row][col] = 0  # Undo move (backtrack)
                return False  # No valid number found, trigger backtracking

    return True  # Solved


# Example 9x9 Sudoku grid (0 represents empty spaces)
sudoku_grid = [
    [5, 3, 0,  0, 7, 0,  0, 0, 0],
    [6, 0, 0,  1, 9, 5,  0, 0, 0],
    [0, 9, 8,  0, 0, 0,  0, 6, 0],

    [8, 0, 0,  0, 6, 0,  0, 0, 3],
    [4, 0, 0,  8, 0, 3,  0, 0, 1],
    [7, 0, 0,  0, 2, 0,  0, 0, 6],

    [0, 6, 0,  0, 0, 0,  2, 8, 0],
    [0, 0, 0,  4, 1, 9,  0, 0, 5],
    [0, 0, 0,  0, 8, 0,  0, 7, 9]
]

print "Original Sudoku Grid:"
print_grid(sudoku_grid)

if solve_sudoku(sudoku_grid):
    print "\nSolved Sudoku Grid:"
    print_grid(sudoku_grid)
else:
    print "\nNo solution exists."
