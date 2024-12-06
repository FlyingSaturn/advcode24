'''
There's a story with this code. I literally wrote this on the bus.
'''


from re import findall


S = 0


def main():
    text = ""
    with open("../inputs/input_day3.txt") as file:
        text = file.read()
    matches = findall(r'mul\([0-9]{1,3}\,[0-9]{1,3}\)', text);
    text=""
    for match in matches:
        extract(match)
    print(S)


def extract(s):
    li=findall('[0-9]+', s)
    sigma_rule(li)


def sigma_rule(l):
    global S
    S = S + int(l[0]) * int(l[1])


main()
