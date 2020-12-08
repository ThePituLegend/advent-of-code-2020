required_fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
count = 0

with open("input.txt", "r") as file:
    input = file.read().split("\n\n")

for passport in input:
    if all(field in passport for field in required_fields):
        count += 1

print(count)
