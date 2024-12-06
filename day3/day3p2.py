'''
Part 2 was easy if it was done in regex. I myself did it within 2 minutes. 
Regex is useful. Please learn it.
'''
from re import findall

S = 0
def main():
    text = ""
    domode=True
    with open("../inputs/input_day3.txt") as file:
        text = file.read()
    matches = findall(r'(do\(\)|don\'t\(\)|mul\([0-9]{1,3}\,[0-9]{1,3}\))', text);
    text=""
    for match in matches:
        if match == "don\'t()":
            domode=False
        elif match == "do()":
            domode=True
        if domode and not(match == 'do()' or match == 'don\'t()') :
            extract(match)
    print(S)


def extract(s):
    li=findall('[0-9]+', s)
    sigma_rule(li)


def sigma_rule(l):
    global S
    S = S + int(l[0]) * int(l[1])


main()
