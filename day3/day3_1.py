input = []
coord = 0 # x coord
count = 0

with open("input.txt", "r") as file:
    for line in file:
        input.append(list(line.strip()))

size = len(input[0]) # x size

for line in input[1:]:
    coord += 3
    coord %= size

    if line[coord] == "#":
        count += 1

print(count)
