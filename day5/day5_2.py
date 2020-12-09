# After 10's of puzzles with tunnelvision, I've realised I don't need to cache the whole file for
# most of the puzzles. Maybe I'll come back later to improve that, if I have time.

IDS = []

with open("input.txt", "r") as file:
    for bsp in file:
        bsp = bsp.strip();

        row = int(bsp[:7].replace("F", "0").replace("B", "1"), 2)
        column = int(bsp[-3:].replace("L", "0").replace("R", "1"),2)

        id = row * 8 + column
        IDS.append(id)

IDS.sort()
print(IDS)

for id in IDS:
    if id+1 not in IDS and id+2 in IDS:
        print(id+1)
        break;
