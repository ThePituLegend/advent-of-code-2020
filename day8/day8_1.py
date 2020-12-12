from console import Console

with open("input.txt", "r") as file:
    RAM = file.read().strip().splitlines()

RAM = [instruction.split() for instruction in RAM]

console = Console(RAM)

console.execute_RAM()

print(console)

