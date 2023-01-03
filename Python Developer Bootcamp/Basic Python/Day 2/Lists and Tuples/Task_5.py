from Task_4 import suma


def mean(numbers):
    average = suma(numbers) / len(numbers)
    return average


if __name__ == "__main__":
    print(mean([1, 2, 3]))
