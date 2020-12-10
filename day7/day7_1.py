holdingBags = []

def findBag(name, rules):
    if len(rules[name]) == 0:
        return False
    elif "shiny gold" in list(rules[name].keys()) + holdingBags:
        return True
    else:
        found = False
        for subr in rules[name]:
            found |= findBag(subr, rules)
        return found


with open("input.txt", "r") as file:
    rules = file.read().strip().splitlines()

rules = dict(rule.split(" contain ") for rule in rules)

newRules = {}
for name, rule in rules.items():
    name = " ".join(name.split()[:-1])
    
    newRules[name] = {}
    
    if rule == "no other bags.":
        rule = ""
    else:
        rule = rule.split(", ")
        
        for subr in rule:
            newRules[name][" ".join(subr.split()[1:-1])] = subr[0]

for name, rule in newRules.items():
    if name != "shiny gold":
        if findBag(name, newRules):
            holdingBags.append(name)

print(len(holdingBags))
