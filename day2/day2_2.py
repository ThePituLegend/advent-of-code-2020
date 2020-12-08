input = []
count = 0

with open("input.txt", "r") as file:
    for line in file:
        input.append(line.rstrip().split(":"))
        
        input[-1][1] = input[-1][1].strip()

        input[-1][0] = input[-1][0].split()
        
        input[-1][0][0] = input[-1][0][0].split("-")
        input[-1][0][0][0] = int(input[-1][0][0][0])
        input[-1][0][0][1] = int(input[-1][0][0][1])

pwd = input[0]

for pwd in input:
    if (pwd[1][pwd[0][0][0]-1] == pwd[0][1]) != (pwd[1][pwd[0][0][1]-1] == pwd[0][1]):
        count += 1

print(count)
