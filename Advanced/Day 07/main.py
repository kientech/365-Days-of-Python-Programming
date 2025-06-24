# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 07

# Simple Sudoku Solver using backtracking

def find_empty_location(grid, l):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

def used_in_row(grid, row, num):
    for i in range(9):
        if grid[row][i] == num:
            return True
    return False

def used_in_col(grid, col, num):
    for i in range(9):
        if grid[i][col] == num:
            return True
    return False

def used_in_box(grid, row, col, num):
    for i in range(3):
        for j in range(3):
            if grid[i + row][j + col] == num:
                return True
    return False

def is_safe_location(grid, row, col, num):
    return not used_in_row(grid, row, num) and \
           not used_in_col(grid, col, num) and \
           not used_in_box(grid, row - row % 3, col - col % 3, num)

def solve_sudoku(grid):
    l = [0, 0]
    if not find_empty_location(grid, l):
        return True
    
    row, col = l[0], l[1]
    
    for num in range(1, 10):
        if is_safe_location(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
            
    return False

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

# Example Sudoku puzzle
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Puzzle:")
print_grid(puzzle)

if solve_sudoku(puzzle):
    print("\nSolution:")
    print_grid(puzzle)
else:
    print("\nNo solution exists") 