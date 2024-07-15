import sys
import numpy as np

dict = {
    "*":-2,
    "#":-1,
    "O":0,
    "%":1,
    "A":2
}
head = ""
n = 0
m = 0
k = 0
e = ""
size = 0
board = list()
tunnels = list()
tunnel_dict = {}

prob_map = []

def moves(pos, direction):

    return ""

def create_tunnel(tunnels, e):
    for i in range(0,len(e),4):
            tunnels.append([[(e[i], e[i+1]), (e[i+2], e[i+3])]])
    for t in tunnels:
        # Zero indexing
        t[0] = np.subtract(t[0],(1,1))
        t[1] = np.subtract(t[1],(1,1))
        # Adding to the tunnel dictionary
        tunnel_dict[tuple(t[0])] = tuple(t[1])
        tunnel_dict[tuple(t[1])] = tuple(t[0])
        # Marking the tunnels on the board.
        board[tuple(t[0])] = "T"
        board[tuple(t[1])] = "T"


if __name__ == '__main__':
    # Function to allow to send your own set files via command line.
    if len(sys.argv) > 1:
        with open(sys.argv[1],"r") as file:
            lines = file.readlines()
        # If there is anything in second argument, then DEBUG gets turned on. 
        if len(sys.argv) > 2:
            DEBUG = True
        head = lines.pop()
        n,m,k = [int(head[0]), int(head[1]), int(head[2])]
        size = n*m
        prob_map = np.zeros(shape=(size,size),dtype=float)
        e = lines[-1]
        del lines[-1]
        m = list()
        for l in lines:
            m.append(list(l))
        board = np.array(m)
        tunnels = np.array(tunnels)
    else:
        DEBUG = True
        n,m,k = [3, 6, 1]
        maze = [["#", "#", "#", "*", "O", "O"], 
                ["O", "#", "O", "A", "%", "O"], 
                ["#", "#", "#", "*", "O", "O"]]
        tunnels = [[(2,3), (2,1)]] 
    size = n*m
    create_tunnel(tunnels,e)
    moves([])
