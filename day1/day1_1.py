input = []
visited = []

with open("input.txt", mode="r") as file:
    for line in file:
        input.append(int(line))

for num in input:
    visited.append(num)
    other = abs(num-2020)
    if (other in visited):
        print(num*other)
        break;
