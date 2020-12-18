from math import floor

def find_nearest_multiple(x, n):
    return x * floor(n/x) + x

with open("input.txt", "r") as file:
    input = file.read().strip().splitlines()

target = int(input[0])
lines = sorted([(find_nearest_multiple(int(bus), target), int(bus)) for bus in input[1].split(",") if bus != "x"])

print(lines[0][1]*(lines[0][0]-target))
