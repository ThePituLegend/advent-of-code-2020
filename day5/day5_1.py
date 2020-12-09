# After 10's of puzzles with tunnelvision, I've realised I don't need to cache the whole file for
# most of the puzzles. Maybe I'll come back later to improve that, if I have time.

ID = []

with open("input.txt", "r") as file:
    for bsp in file:
        bsp = bsp.strip();
        row = int(bsp[:7].replace("F", "0").replace("B", "1"), 2)
        column = int(bsp[-2:].replace("L", "0").replace("R", "1"),2)
        ID.append(row * 8 + column)

print(max(ID))
