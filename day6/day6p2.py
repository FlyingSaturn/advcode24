from itertools import cycle
from re import search

# p = 1 # No. of positions visited
direct = {
        'u': (-1, 0),
        'r': (0, 1),
       'd': (1, 0),
        'l': (0, -1)
        }
pos=[]
initpos=[]
labinit=[]
labfin=[]
direction=''
# For obstruction
obperfect_chumu=0

def main():
    global labinit, direction, pos, initpos
    k = 0
    found = False
    with open("input_day6.txt") as file:
        for line in file:
            if not found:
                k += 1
            linearr = list(line.strip())
            if search(r'(\^|>|v|<)', line.strip()):
                found = True
                initpos.append(k-1)
                if '^' in line:
                    direction = 'u'
                    initpos.append(linearr.index('^'))  
                if '>' in line:
                    direction = 'r'
                    initpos.append(linearr.index('>'))  
                if 'v' in line:
                    direction = 'd'
                    initpos.append(linearr.index('v'))
                if '<' in line:
                    direction = 'l'
                    initpos.append(linearr.index('<'))  
            labinit.append(linearr)
    pos = list(initpos)
    traverse_ultima()
   

def check(l):
    global pos, direction
    n_i = pos[0] + direct[direction][0]
    n_j = pos[1] + direct[direction][1]
    
    # Finished
    if n_i >= len(l) or n_j >= len(l[0]) or n_i < 0 or n_j < 0:
        if l[pos[0]][pos[1]] not in ['^', 'v', '<', '>']:
            l[pos[0]][pos[1]] = 'X'
        return -1
    
    # A turn is a move here
    if l[n_i][n_j] in ['#', 'O']:
        D = list(direct.keys())
        direction = D[(D.index(direction) + 1) % 4]
        if l[n_i][n_j] in ['#', 'O']:
            return 299792458
        return check(l)

    # Replace the remaining
    if l[pos[0]][pos[1]] not in ['^', 'v', '<', '>']:
        l[pos[0]][pos[1]] = 'X'
    pos[0] = n_i
    pos[1] = n_j

    # Already traversed
    if l[n_i][n_j] in ['X', '^']:
        return 2

    # Not already traversed remains
    return 0

def traverse():
    lab = labinit
    a = 0
    # p = 0
    while a != -1:
        a = check(lab)
        # if a == 0:
            # p += 1
    # print(p)
    labfin = lab
    
def obstructed(i, j):
    global labinit, obperfect_chumu
    # Place the obstructor on a duplicate scenario after you get a call from traverse()
    # Traverse with that obstructor
    # If the thing is perfectly traversing AGAIN by that obstructor, make a minimum
    lab1 = labinit
    lab1[i][j] = 'O'
    a = 0
    p = 0
    firsttime = True
    while a != -1:
        a = check(lab1)
        if a == 0:
            p += 1
        if a == 299792458 and firsttime == False:
            break
        else:
            firsttime = False
    if a == 299792458 and firsttime == False:
        obperfect_chumu += 1
        return True
    return False

def traverse_ultima():
    global obperfect_chumu
    traverse()
    for i in range(0, len(labfin)):
        for j in range(0, len(labfin[0])):
            if labfin[i][j] == 'X':
                obstructed(i, j)

    print(obperfect_chumu)



main()
