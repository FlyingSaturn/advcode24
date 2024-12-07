from re import findall

S = 0
order = []
pages = []
def main():
    global S
    with open('../inputs/input_day5_order.txt') as file:
        for line in file:
            l = tuple(findall("[0-9]+", line.strip()))
            order.append(l)
    with open('../inputs/input_day5_pages.txt') as file:
        for line in file:
            l = findall('[0-9]+', line.strip())
            pages.append(l)
    poscheck()
    print(S)


def check(li):
    for (a, b) in order:
        try:
            if li.index(a) > li.index(b):
                return False 
        except ValueError:
            pass
    return True

def poscheck():
    global S
    for i in pages:
        if check(i):
            S += int(i[(len(i) - 1) // 2])

main()
