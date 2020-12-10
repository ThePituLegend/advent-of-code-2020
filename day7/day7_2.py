def sumBags(name, rules):
    if len(rules[name]) == 0:
        return 0
    else:
        count = 0
        for subr, ammount in rules[name].items():
            count += int(ammount) + int(ammount) * sumBags(subr, rules)
        return count

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

count = 0;
for name, ammount in newRules["shiny gold"].items():
    count += int(ammount) + int(ammount) * sumBags(name, newRules)

print(count)
