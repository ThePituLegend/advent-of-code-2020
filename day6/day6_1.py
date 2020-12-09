with open("input.txt", "r") as file:
    groups = file.read().split("\n\n")    

groups = [len(set(group.replace("\n", ""))) for group in groups]
print(sum(groups))
