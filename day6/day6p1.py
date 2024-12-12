from itertools import cycle
from re import search

p = 1 # No. of positions visited
direct = {
        'u': (-1, 0),
        'r': (0, 1),
       'd': (1, 0),
        'l': (0, -1)
        }
pos=[]
lab=[]
direction=''

def main():
    global direction, pos, lab 
    k = 0
    found = False
    with open("../inputs/input_day6.txt") as file:
        for line in file:
            if not found:
                k += 1
            linearr = list(line.strip())
            if search(r'(\^|>|v|<)', line.strip()):
                found = True
                pos.append(k)
                if '^' in line:
                    direction = 'u'
                    pos.append(linearr.index('^'))  
                if '>' in line:
                    direction = 'r'
                    pos.append(linearr.index('>'))  
                if 'v' in line:
                    direction = 'd'
                    pos.append(linearr.index('v'))
                if '<' in line:
                    direction = 'l'
                    pos.append(linearr.index('<'))  
            lab.append(linearr)
    traverse()
   

def check():
    global p, pos, direction, lab
    n_i = pos[0] + direct[direction][0]
    n_j = pos[1] + direct[direction][1]
    
    # Finished
    if n_i >= len(lab) or n_j >= len(lab[0]) or n_i < 0 or n_j < 0:
        return -1
    
    # A turn is a move here
    if lab[n_i][n_j] == '#':
        D = list(direct.keys())
        direction = D[(D.index(direction) + 1) % 4]
        return check()

    # Replace the remaining
    lab[pos[0]][pos[1]] = 'X'
    pos[0] = n_i
    pos[1] = n_j

    # Already traversed
    if lab[n_i][n_j] == 'X':
        return 2

    # Not already traversed remains
    p += 1
    return 0

def traverse():
    global p
    a = 0
    while a != -1:
        a = check()
    print(p)
    

main()
