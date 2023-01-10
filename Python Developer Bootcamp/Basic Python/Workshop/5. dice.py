from random import randint


def roll(input):
    D = input.find("D")
    if D < 0:
        raise Exception("Invalid data")
    num = int(input[0:D])
    plus = input.find("+")
    minus = input.find("-")
    if plus > 0:
        dice = int(input[D + 1:plus])
        modifier = int(input[plus:])
    elif minus > 0:
        dice = int(input[D + 1:minus])
        modifier = int(input[minus:])
    else:
        dice = int(input[D + 1:])
        modifier = 0
    print(f"dice = {dice}")
    print(f"num = {num}")
    print(f"mod = {modifier}")
    dices = [3, 4, 6, 8, 10, 12, 100]
    if dice not in dices:
        raise Exception("No such dice!")
    total = 0
    for i in range(num):
        total += randint(1, dice)
    print(f"Total = {total + modifier}")


if __name__ == "__main__":
    roll("5D100+13")
    print("---")
    roll("5D6-13")
    print("---")
    roll("5D7")