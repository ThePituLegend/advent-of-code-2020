input = []
count = 0

with open("input.txt", "r") as file:
    for line in file:
        input.append(line.rstrip().split(":"))
        
        input[-1][0] = input[-1][0].split()
        
        input[-1][0][0] = input[-1][0][0].split("-")
        input[-1][0][0][0] = int(input[-1][0][0][0])
        input[-1][0][0][1] = int(input[-1][0][0][1])

for pwd in input:
    cnt = pwd[1].count(pwd[0][1])
    if cnt >= pwd[0][0][0] and cnt <= pwd[0][0][1]:
        count += 1

print(count)
