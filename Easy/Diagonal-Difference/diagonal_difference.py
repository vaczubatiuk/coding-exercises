import sys

DEBUG = False
entry = list()

# =========================================================
# Function: diagonalDifference
# Parameters: a 2d list of integers in a square matrix
# Output: the absolute difference in diagonal values.
# =========================================================
def diagonalDifference(arr):
    # Setting the first 
    leftdiagonal = 0
    rightdiagonal = 0
    for i in range(len(arr)):
        leftdiagonal += arr[i][i]
        rightdiagonal += arr[-i-1][i]
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
    
