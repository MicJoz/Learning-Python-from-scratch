from random import randint


def random_average(n):
    total = 0
    for i in range(n):
        total += randint(1, 100)
    return total / n


if __name__ == "__main__":
    print(random_average(5))
    print(random_average(10))
