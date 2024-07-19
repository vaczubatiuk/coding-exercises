import sys
import os

DEBUG = False
log = open("OUTPUT.log","w")
entry = list()

# ==============================================================================
# Function: print_or_log
# Paramter: A single string
# Output:   Either prints to CL or prints to log depending on debugging mode.
# ==============================================================================

def print_or_log(string):
    print(string) if DEBUG else log.write(string)
# ==============================================================================
# Our Function from the Left-Rotation Exercise, comes in handly with our approach
# Function: leftRotation
# Parameters: a list of generic values (typeless)0
# Output: a list where it is rotated left by one position: 
#         i.e: [1, 2, 3, 4, 5] => [2, 3, 4, 5, 1] 
# ==============================================================================
def leftRotation(arr):
    r = list(arr)
    t = r.pop(0)
    r.append(t)
    return r
# ==============================================================================
# Function: minMaxSum
# Parameter: a list of integers.
# Output: prints min and max results to the command line.
# ==============================================================================
def minMaxSum(arr):
    # Setting min and max to infinity and negative infinity respectfuly.
    minResult,maxResult = (float('inf'),float('-inf'))
    # Cloning the list so we don't manipuate the original.
    result = list(arr)
    # Looping through the elements of result
    for i in range(len(result)):
        # Clone the list for manipulations without affecing the loop.
        tempL = list(result)
        # Pop the first entry to reduce the elements to 4
        tempL.pop(0)
        # Add together all the left over elements
        sumL = sum(tempL)
        # Compare and set min and max values
        minResult = sumL if sumL < minResult else minResult
        maxResult = sumL if sumL > maxResult else maxResult
        # Left rotate the list once so for the next loop iteration.
        result = leftRotation(result)
    # Print the result.
    print(f"{minResult} {maxResult}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1],'r') as file:
            entry = file.readlines()
    else:
        entry = [1, 2, 3, 4, 5]
    if (os.path.isfile("OUTPUT.log")):
        log.close()
    if (os.path.getsize("OUTPUT.log") == 0):
        os.remove("OUTPUT.log")
    minMaxSum(entry)

