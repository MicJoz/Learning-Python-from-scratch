import random


def single_trial():
    first_flip = random.randint(0, 1)
    flips_per_trial = 2  # first flip + second flip
    while first_flip == random.randint(0, 1):
        flips_per_trial += 1
    return flips_per_trial


def experiment(value):
    total_flips = 0
    for i in range(value):
        total_flips += single_trial()
    return total_flips


value = 10000
print(F"The average number of flips per trial was {experiment(value) / value}")
