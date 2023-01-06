import random
from random import randint

def d6(num):
    total = 0
    for i in range(num):
        total += random.randint(1, 6)
    return total


if __name__ == "__main__":
    num = int(input("Enter how many times to throw a dice: "))
    print(f" Total is: {d6(num)}")
    