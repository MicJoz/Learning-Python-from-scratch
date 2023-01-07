from random import randint


def roll(num, dice=6, modifier=0):
    dices = [3, 4, 6, 8, 10, 12, 100]
    if dice not in dices:
        raise Exception("No such dice!")
    total = 0
    for i in range(num):
        total += randint(1, dice)
    return total + modifier


if __name__ == "__main__":
    print(roll(5, 100, 20))
