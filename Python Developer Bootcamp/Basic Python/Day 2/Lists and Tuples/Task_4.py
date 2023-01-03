def suma(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


if __name__ == "__main__":
    print(suma([1, 2, 3]))
