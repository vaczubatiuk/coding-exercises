
import sys
import pprint
DEBUG = False
log = open("OUTPUT.log","w")
# Function: missleDefend
# Parameter: Two dimensional list (list of lists) of integer:
#               - subelement 0 = reflects time (t)
#               - subelement 1 = frequency
# Output: A single integer representing the number of missiles used.
# Methods: Minimum Path Cover using DAG.

def print_or_log(string):
    print(string) if DEBUG else log.write(string)
def missileDefend(missles):

    # Instantiated sorted couples of sums and differences between time and frequency, generating our DAG, with a list of vertex points.
    # [[1, 1], [2, 3], [3, 1], [5, 1]] => [(2, 0), (4, 2), (5, -1), (6, 4)]
    DAG = sorted(list((a+b,a-b) for a,b in missles))
    # Pulling the y-axis points of the vertex list into a iterable list:
    # [(2, 0), (4, 2), (5, -1), (6, 4)] => [0, 2, -1, 4]
    y_points = list(y for x,y in DAG)
    # Instatiated empty list to collect our results
    results = []
    # Looping through items in 
    for y in y_points:
        # Setting our lowest index (-1 represents )
        (count := 0) if DEBUG else ""
        low = -1
        # setting our highest value
        high = len(results)
        print_or_log("""
=====================================""")
        print_or_log(f"""Y positition: {y} for array: {missles} 
with coefficents: {y_points}""")
        print_or_log("""=====================================""")
        # While block will only when there are at least 1 entries in integer list, results. (0 - 1 =  1 )
        # At the same time, once the difference of high and low below 1, then it means that high reached the end of its comparative search. (hitting negative)
        while high-low > 1:
            (count := count+1) if DEBUG else ""

            print_or_log(f"""
Iteration {count}
Current Results: {results}""")
            # Gets the representational index for our acyclic path in our DAG.
            mid = (low + high) >> 1
            print_or_log(f"Mid: {mid} | High: {high} | Low: {low}")
            # ======================================================================================================================================
            # Checks if element at position mid is greater than item.
            # If true : low is assigned to mid | Else: high is assigned to mid.
            #
            #  - When result at idx mid is greater than the elem in y_points, we assign low to the value of mid, 
            #    as mid index points to the now lowest significant element now resides and indicates a new missile is needed. 
            #    Setting/Shifting the low index for the next iteration of the while loop.
            #
            #  - When results at idx mid is less than the elem in y_points, 
            #    we change high value's to mid (which will always be smaller than len(results) due to the bit shift operator). 
            #    Thus Setting/Shifting the high index for the next iteration of the while loop.
            # 
            # ======================================================================================================================================
            if results[mid] > y:
                low = mid
                print_or_log(f"New low assignment: {low}")
            else:
                high = mid
                print_or_log(f"New high assignment: {high}")
            
        # If the value for integer variable high has not been changed during the while loop,
        # it means another missile is required currernt vertex point and y is appended to results.
        if high == len(results):
            results.append(y)
        # Else, it was discovered that a missile was not needed at current vertex point. 
        # We then set value of results at idx mid to the value of y. This represents a possible small change in frequency of our current missile but not enough to warrant a new missile.
        else:
            results[high] = y

    print_or_log(f"""
Final Results: {results}
""")
    return len(results)


if __name__ == '__main__':
    ### Code from HackerX Site, not needed for Github repo ###
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # # Gets the number of rows from the first entry
    # n = int(input().strip())
    # # Maps the rest into a 2D array
    # inp = (map(int, input().split()) for i in range(n))
    # fptr.write(str(missileDefend(inp)))
    # fptr.close
    if len(sys.argv) > 1:
        with open(sys.argv[1],"r") as file:
            lines = file.readlines()
        if len(lines[0] == 1):
            lines.pop()
        if len(sys.argv) > 2:
            DEBUG = True
    else:
        #lines = [(1,1),(2,3),(3,1),(5,1)]
        DEBUG = True
        lines = [(65,844),(70,993),(201,427),(348,899),(388,268),(440,416),(459,421),(459,796),(744,291),(870,121)]
    print_or_log(f"""Total number of missiles required: {str(missileDefend(lines))}
For the following time and frequency of each incomming missiles:
{lines}""")
    #{pprint.pprint(lines)}
