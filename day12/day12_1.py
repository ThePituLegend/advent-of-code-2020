with open("input.txt", "r") as file:
    input = [(line[0], int(line[1:])) for line in file.read().strip().splitlines()]

facing = 90
pos = [0,0]

rotations = "NESW"
actions = {"N": (0,1), "S": (0,-1), "E": (1,0), "W": (-1,0), "R" : 1, "L" : -1}

print(input)
print("<------------------->")

print(facing, "|", pos)
for step in input:
    if step[0] in ["R", "L"]:
        facing += actions[step[0]] * step[1]
        facing %= 360
    elif step[0] == "F":
        face = rotations[facing//90]
        pos[0] += actions[face][0] * step[1]
        pos[1] += actions[face][1] * step[1]
    else:
        pos[0] += actions[step[0]][0] * step[1]
        pos[1] += actions[step[0]][1] * step[1]
    print(facing, "|", pos)

print("Manhattan distance:", abs(pos[0])+abs(pos[1]))
