list = [4,6,4,3,3,3,4,2,2]
for i in list:
    list1 = list.copy()
    list1.remove(i)
    for j in list1:
        print(j, " ", end="")
    print()
