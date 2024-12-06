first = []
second = []

with open("input_day1p1.txt") as file:
    for line in file:
        row = line.rstrip().split("   ")
        first.append(int(row[0]))
        second.append(int(row[1]))

first.sort()
second.sort()

similarity = 0
for i in first:
    k = 0
    for j in second:
        if j == i:
            k = k + 1
        if j > i:
            break
    similarity = similarity + k*i

print(similarity)
