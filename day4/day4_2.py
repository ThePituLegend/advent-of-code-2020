import re

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

count = 0

with open("input.txt", "r") as file:
    input = file.read().split("\n\n")

input = [re.split(" |\n", passport) for passport in input]

input = [dict(pairs.split(":") for pairs in passport if pairs != "") for passport in input]

for passport in input:
    if all(key in passport for key in required_fields):
        if 1920 <= int(passport["byr"]) <= 2002:
            if 2010 <= int(passport["iyr"]) <= 2020:
                if 2020 <= int(passport["eyr"]) <= 2030:
                    if ("cm" in passport["hgt"] and 150 <= int(passport["hgt"][:-2]) <= 193) or \
                        ("in" in passport["hgt"] and 59 <= int(passport["hgt"][:-2]) <= 76):
                        if re.match(r"^#[0-9a-f]{6}$", passport["hcl"]):
                            if passport["ecl"] in ecl:
                                if re.match(r"^[0-9]{9}$", passport["pid"]):
                                        count += 1

print(count)
