import sys

DEBUG = False
log = open("OUTPUT.log","w")

# Function: print_or_log
# Paramter: A single string
# Output:   Either prints to CL or prints to log depending on debugging mode.
def print_or_log(string):
    print(string) if DEBUG else log.write(string)


# Function: leftRotation
# Parameter: one integer and one list
# Output: a left rotated list.
def leftRotation(c,array):
    # Cloning the array, it makes for better flow control. 
    result = list(array)
    print_or_log(result)
    # Rotating through the list to perform the left rotations.
    for i in range(c):
        # Pop the first 
        item = result.pop(0)
        print_or_log(af
f"""
The next idx 0 value to push to the back: {item}
""" 
    )
        # Append original result[0] to result[n-1], where as n is equivalent to the length of the list
        result.append(item)
        print_or_log(result)
    return result

if __name__ == '__main__':
    # Variable declaration
    count = 0
    data = list()
    # Command Line Argument handling.
    if len(sys.argv) > 1:
        # Calling up the file in a with block.
        with open(sys.argv[1],"r") as file:
            # Pulling all the file lines into a list
            data = file.readlines()
            # Popping the first line for the number of left rotations needed
            c = data.pop()
            # Stripping whitespaces
            c = c.replace(" ", "")
            # Grabbing the number of left rotations
            count = int(c[1])
        # If a second argument exists, it is for DEBUG, regardless of value.
        if len(sys.argv) > 2:
            DEBUG = True
    # Default handling.
    else:
        count = 4
        print_or_log(
f"""
Established number of left rotations: {count}
"""
)
        data = [1,2,3,4,5]
        print_or_log(data)
        output = leftRotation(count,data)
        DEBUG = True
    print(output)
    log.close()