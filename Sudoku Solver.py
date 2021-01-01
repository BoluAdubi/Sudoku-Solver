def readGrid(file): # read sudoku 9x9 grid from file
    myInfile = open(file, "r")

    # check if file is open
    if myInfile.closed:
        print(myInfile.name + " is closed")
    else:
        print(myInfile.name + " is open")

    twoDArray = []

    # read in lines and store in 2D array
    for x in myInfile.readlines():
        twoDArray.append(x)

    # print array
    for x in twoDArray:
        for y in x:
            print(y, end = " ")
        print()

    myInfile.close()

def main():
    readGrid("input.txt")

main()