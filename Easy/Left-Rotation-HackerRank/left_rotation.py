import sys

DEBUG = False
log = open("OUTPUT.log","w")
def print_or_log(string):
    print(string) if DEBUG else log.write(string)

def leftRotation(c,array):
    result = list(array)
    print(result)
    for i in range(c):
        item = result.pop(0)
        print(item)
        result.append(item)
        print(result)
    return result



if __name__ == '__main__':
    count = 0
    data = list()
    if len(sys.argv) > 1:
        with open(sys.argv[1],"r") as file:
            data = file.readlines()
            c = data.pop()
            c = c.replace(" ", "")
            count = int(c[1])
            
        if len(sys.argv) > 2:
            DEBUG = True
    else:
        count = 4
        print(count)
        data = [1,2,3,4,5]
        print(data)
        output = leftRotation(count,data)
    print(output)
    log.close()