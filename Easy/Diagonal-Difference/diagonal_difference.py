import sys

DEBUG = False
entry = list()

# =========================================================
# Function: diagonalDifference
# Parameters: a 2d list of integers in a square matrix
# Output: the absolute difference in diagonal values.
# =========================================================
def diagonalDifference(arr):
    # Setting the left diagonal sum variable 
    leftdiagonal = 0
    # Setting the right diagonal sum variable
    rightdiagonal = 0
    for i in range(len(arr)):
        # for left diag [x,y] where x == y
        leftdiagonal += arr[i][i]
        # for rigth diag [x,y] x == -y-1 as indeces in python lists have negative representations that we can use
        # to x's corresponding negative index: multiply x by -1 then subtract 1 
        # or another way to look at it add 1 to x and take it's negative
        # Example: 
        # x = 0 -> -1(0) = 0 -> 0-1 = -1
        # x = 1 -> -1(1) = 1 -> -1-1 = -2
        # etc.
        rightdiagonal += arr[-i-1][i]
    # Returning the absoulte value of the difference between 
    # the left diagonal sum and the right diagonal sum
    return abs(leftdiagonal - rightdiagonal)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        entryT = list()
        with open(sys.argv[1],'r') as file:
            entryT = file.readlines()
        entryT.pop(0)
        for e in entryT:
            entry.append(list(map(int,e)))
        if len(sys.argv) > 2:
            DEBUG = True
    else:
        entry = [[11,2,4],[4,5,6],[10,8,-12]]
    print(diagonalDifference(entry))
    
