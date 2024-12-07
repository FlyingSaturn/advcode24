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


def correct(li):
    for (a, b) in order:
        try:
            a_l = li.index(a)
            b_l = li.index(b)
            if a_l > b_l:
                li[a_l], li[b_l] = li[b_l], li[a_l]
        except ValueError:
            pass
    return

def poscheck():
    global S
    for i in pages:
        correct(i)
        S += int(i[(len(i) - 1) // 2])

main()
