from math import prod

input = []
coord = 0 # x coord
count = [0, 0, 0, 0, 0]

with open("input.txt", "r") as file:
    for line in file:
        input.append(list(line.strip()))

size = len(input[0]) # x size

coord = 0
for line in input[1:]:
    coord += 1
    coord %= size

    if line[coord] == "#":
        count[0] += 1

coord = 0
for line in input[1:]:
    coord += 3
    coord %= size

    if line[coord] == "#":
        count[1] += 1

coord = 0
for line in input[1:]:
    coord += 5
    coord %= size

    if line[coord] == "#":
        count[2] += 1

coord = 0
for line in input[1:]:
    coord += 7
    coord %= size

    if line[coord] == "#":
        count[3] += 1

coord = 0
for line in input[2::2]:
    coord += 1
    coord %= size

    if line[coord] == "#":
        count[4] += 1

print(prod(count))
