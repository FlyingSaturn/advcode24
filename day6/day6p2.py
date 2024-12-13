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
visited=[]
cookies = False

def main():
    global labinit, direction, pos, initpos
    k = 0
    found = False
    with open("../inputs/input_day6.txt") as file:
        for line in file:
            if not found:
                k += 1
            linearr = list(line.strip())
            if search(r'(\^|>|v|<)', line.strip()):
                found = True
                initpos.append(k-1)
                if '^' in line:
                    initpos.append(linearr.index('^'))  
                    initpos.append('u')
                if '>' in line:
                    initpos.append(linearr.index('>'))  
                    initpos.append('r')
                if 'v' in line:
                    initpos.append(linearr.index('v'))
                    initpos.append('d')
                if '<' in line:
                    initpos.append(linearr.index('<'))  
                    initpos.append('l')
            labinit.append(linearr)
    pos = list(initpos)
    traverse_ultima()
   

def check(l):
    global pos, visited, cookies

    n_i = pos[0] + direct[pos[2]][0]
    n_j = pos[1] + direct[pos[2]][1]
    
    # Finished
    if n_i >= len(l) or n_j >= len(l[0]) or n_i < 0 or n_j < 0:
        if l[pos[0]][pos[1]] not in ['^', 'v', '<', '>']:
            l[pos[0]][pos[1]] = 'X'
        return -1
    
    # A turn is a move here
    if l[n_i][n_j] in ['#', 'O']:
        if 'O' == l[n_i][n_j]:
            cookies=True
        D = list(direct.keys())
        pos[2] = D[(D.index(pos[2]) + 1) % 4]
        return check(l)
    if cookies:
        if [n_i, n_j, pos[2]] not in visited:
            visited.append([n_i, n_j, pos[2]])
        else:
            return 299792458


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
    global labinit, labfin
    lab = [row[:] for row in labinit]
    a = 0
    # p = 0
    while a != -1:
        a = check(lab)
        # if a == 0:
            # p += 1
    # print(p)
    labfin = [row[:] for row in lab]

    
def obstructed(i, j):
    global labinit, pos, initpos, visited, cookies
    # Place the obstructor on a duplicate scenario after you get a call from traverse()
    # Traverse with that obstructor
    # If the thing is perfectly traversing AGAIN by that obstructor, make a minimum
    lab1 = [row[:] for row in labinit]
    lab1[i][j] = 'O'
    pos = list(initpos)
    a = 0
    # p = 0
    visited = []
    cookies = False
    while a != -1:
        a = check(lab1)
                # if a == 0:
            # p += 1
        if a == 299792458:
            cookies = False
            return True
    cookies = False
    return False

def traverse_ultima():
    # For obstruction
    obperfect_chumu = 0
    traverse() 
    for i in range(0, len(labfin)):
        for j in range(0, len(labfin[0])):
            if labfin[i][j] == 'X':
                if obstructed(i, j):
                    obperfect_chumu += 1
    print(obperfect_chumu)



main()
