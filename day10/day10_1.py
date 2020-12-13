from collections import defaultdict

with open("input.txt", "r") as file:
    input = sorted(map(int, file.read().strip().splitlines()))

input.insert(0,0) # Add outlet
input.append(max(input)+3)

distribution = defaultdict(int)

for i in range(len(input)-1):
    distribution[abs(input[i]-input[i+1])] += 1

print(distribution[1]*distribution[3])
