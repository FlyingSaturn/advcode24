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


def correct(li, m, n, flg):
    for (a, b) in order:
        if a in li and b in li:
            if (a != m and b != n) or order[len(order) - 1] == (a, b):
                a_l = li.index(a)
                b_l = li.index(b)
                if a_l > b_l:
                    flg = True
                    li[a_l], li[b_l] = li[b_l], li[a_l]
                    correct(li, a, b, flg)
    if flg:
        return True
    return False

def poscheck():
    global S
    for i in pages:
        if correct(i, *order[len(order) - 1], False):
            S += int(i[(len(i) - 1) // 2])

main()
