import numpy as np
import sys

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

"""
x = x pos (row)
y = y pos (column)
n = number being checked
"""
def isValid(x,y,n):
    global grid

    # check if number is unique vertically
    for i in range(9):
        if grid[i][y] == n:
            return False
    
    # check if number is unique horizontally
    for i in range(9):
        if grid[x][i] == n:
            return False

    # check if number is unique in 3x3 grid
    row = (x//3)*3 
    col = (y//3)*3

    for i in range(3):
        for j in range(3):
            if grid[row + i][col + j] == n:
                return False

    # if number passes all 3 checks, return true
    return True

def printGrid(grid):
    print(np.matrix(grid))

def solve():
    global grid

    # find a blank cell (data in cell = 0)
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                # check if n(1-9) is a possible entry
                # if number is valid, replace 0 with n  
                # if number isn't valid, increase n by 1 (for n in range(1,10))
                for n in range(1,10):
                    if isValid(y,x,n):
                        grid[y][x] = n # put valid number in
                        solve() # call solve() recursively
                        grid[y][x] = 0 # backtrace if needed (replace n with 0)
                return

    printGrid(grid)
    input("Input anything to check if there are more solutions") # check if there are more solutions


def main():

    print("Unsolved Sudoku Grid:\n")
    printGrid(grid)

    print("\nSolved Sudoku Grid:\n")
    solve()

main()