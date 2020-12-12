WIN_SIZE = 25

def valid_number(window, number):
    for n in window:
        dif = abs(number-n)
        if n != dif and dif in window: return True
    return False

def find_wrong(input):
    window = input[:WIN_SIZE]
    i = 1
    for number in input[WIN_SIZE:]:
        if not valid_number(window, number): 
            return number
        else:
            window = input[i:WIN_SIZE+i]
            i += 1
    return False


with open("input.txt", "r") as file:
    input = list(map(int, file.read().strip().splitlines()))

print("WRONG NUMBER:", find_wrong(input))
