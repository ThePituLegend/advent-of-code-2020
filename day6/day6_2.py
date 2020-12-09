with open("input.txt", "r") as file:
    groups = file.read().strip().split("\n\n")

print(groups[:4])

groups = [[set(questions) for questions in group.split("\n")] for group in groups]
print(groups[:4])

print("\n")

groups = [set.intersection(*group) for group in groups]
print(groups[:4])

print("\n")

groups = [len(group) for group in groups]
print(groups[:4])
print(sum(groups))
