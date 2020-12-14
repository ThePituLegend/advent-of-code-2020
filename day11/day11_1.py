def get_next_seat(layout, pos):
    occupied = 0

    for i in range(pos[0]-1, pos[0]+2):
        for j in range(pos[1]-1, pos[1]+2):
            if (i,j) != pos and 0 <= i < len(layout) and 0 <= j < len(layout[i]):
                if layout[i][j] == "#":         
                    occupied += 1

    if layout[pos[0]][pos[1]] == "#" and occupied >= 4:
        return "L"
    if layout[pos[0]][pos[1]] == "L" and occupied == 0:
        return "#"
    return layout[pos[0]][pos[1]]

def compact_state(layout):
    string = []
    for row in layout:
        string.append("".join(row))

    string = "\n".join(string)
    return hash(string)

def get_next_state(layout):
    new_state = []

    for i in range(len(layout)):
        new_state.append([])
        for j in range(len(layout[i])):
            new_state[-1].append(get_next_seat(layout, (i,j)))

    return compact_state(new_state), new_state



with open("input.txt", "r") as file:
    input = file.read().strip().splitlines()

history = [compact_state(input)]

prev_state = input
state_id, last_state = get_next_state(input)

while state_id not in history:
    history.append(state_id)
    prev_state = last_state
    state_id, last_state = get_next_state(last_state)

occupied = 0
for row in prev_state:
    occupied += row.count("#")

print(occupied)
