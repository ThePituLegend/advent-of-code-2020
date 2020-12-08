input = []
visited = []

with open("input.txt", mode="r") as file:
    for line in file:
        input.append(int(line))

# INEFFICIENT AF. DO NOT LOOK AT THIS TOO MUCH :P

for num1 in input:
    for num2 in input:
        for num3 in input:
            if (num1+num2+num3 == 2020) and (num1 != num2 != num3):
                print(num1*num2*num3)
                break;
