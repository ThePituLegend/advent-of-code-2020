PC = 0
ACC = 0

history = []

def nop(_):
    global PC

    PC += 1

def acc(i):
    global PC
    global ACC

    ACC += i
    PC += 1

def jmp(rel):
    global PC

    PC += rel

with open("input.txt", "r") as file:
    RAM = file.read().strip().splitlines()

RAM = [instruction.split() for instruction in RAM]

while PC not in history:
    history.append(PC)    
    eval(RAM[PC][0] + "(" + RAM[PC][1] + ")")

print(ACC)
