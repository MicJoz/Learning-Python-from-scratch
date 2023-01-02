import random


def calculate_net(gross, vat=round(random.random(), 2)):
    netto = gross / (1 + vat / 100)
    return netto


if __name__ == "__main__":
    print(calculate_net(100))
