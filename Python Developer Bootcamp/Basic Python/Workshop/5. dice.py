from random import randint


def counting_total(num, dice, modifier):
    dices = [3, 4, 6, 8, 10, 12, 100]
    if dice not in dices:
        raise Exception("No such dice!")
    total = 0 + modifier
    for i in range(num):
        total += randint(1, dice)
    return total


def dice_roll(input):
    d = input.find("D")
    # print(f"D = {D}")
    if d < 0:
        raise Exception("Invalid data")
    elif d == 0:
        num = 1
    else:
        num = int(input[0:d])
    plus = input.find("+")
    minus = input.find("-")
    if plus > 0:
        dice = int(input[d + 1:plus])
        modifier = int(input[plus:])
    elif minus > 0:
        dice = int(input[d + 1:minus])
        modifier = int(input[minus:])
    else:
        dice = int(input[d + 1:])
        modifier = 0
    # print(f"dice = {dice}")
    # print(f"num = {num}")
    # print(f"mod = {modifier}")
    print(counting_total(num, dice, modifier))


if __name__ == "__main__":
    dice_roll("16D100+130")
    print("---")
    dice_roll("5D12-19")
    print("---")
    dice_roll("D6")
    print("---")
    dice_roll("3D7-2")
