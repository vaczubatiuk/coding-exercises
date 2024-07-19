import sys

def plusMinus(numberSet):
    results = [0,0,0]
    for i in numberSet:
        if i > 0:
            results[0] += 1
        elif i < 0:
            results[1] += 1
        else:
            results[2] += 1
    for j in results:
        perc = j/len(results)
        print("%.6f" % perc)

if __name__ == '__main__':
    
    if len(sys.arvg) > 1:
        numberSet = list()
        with open(sys.argv[1],'r') as file:'
            lines = file.readlines()
            length = lines.pop
            lines = lines.strip(" ")
            for i in lines
                x = int(i)
                numberSet.append(x)
        if len(sys.argv) > 2:
            DEBUG = True
        
    else:
        numberSet = [-4, 3,-9, 0, 4, 1]
        DEBUG = True 
    plusMinus(numberSet)