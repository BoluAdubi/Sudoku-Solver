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
x = x pos
y = y pos
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
            if grid[col + i][row + j] == n:
                return False

    # if number passes all 3 checks, return true
    return True

def main():
    

main()