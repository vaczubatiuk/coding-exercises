import sys
import os

DEBUG = False
log = open("OUTPUT.log","w")
entry = list()

# ==================================================================
# Function: lonelyInteger
# Parameters: a list of integers.
# Output: returns the integer in the list that does not have a twin.
# ==================================================================
def lonelyInteger(arr):
    # Sort and clone the list
    arr2 = sorted(arr)
    # set the starting index at zero
    idx = 0
    # as long as the index is less than the length
    while idx < len(arr2):
        # Here we abuse the index subsetting, so we can avoid the IndexError: Index out of range.
        # If idx+1 is larger than len(arr2)-1 then the subset will be equal to an empty set.
        subset = arr2[idx+1:]
        # Now we compare the subset, if the subset is empty, it means that idx the last element in the list.
        if subset == []:
            # returns the last element in the list.
            return arr2[idx]
        # Check to see if element at index does not equal subset at index 0.
        elif arr2[idx] != subset[0]:
            # if No, then that is our result
            return arr2[idx]
        # Skipping over the current and next result since we are still searching for the lonely integer.
        idx += 2

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1],'r') as file:
            line = file.readlines()

        line = line.strip(" ")
        for i in line:
            entry.append(int(i))
    else:
        entry = [4, 9, 95, 93, 57, 4, 57, 93, 9]
    if (os.path.isfile("OUTPUT.log")):
        log.close()
    if (os.path.getsize("OUTPUT.log") == 0):
        os.remove("OUTPUT.log")


    print(lonelyInteger(entry))

