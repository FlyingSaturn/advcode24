first = []
second = []

with open("../inputs/input_day1p1.txt") as file:
    for line in file:
        row = line.rstrip().split("   ")
        first.append(int(row[0]))
        second.append(int(row[1]))

first.sort()
second.sort()

dist = 0
for i, j in zip(first, second):
    dist = dist + abs(i - j)

print(dist)
