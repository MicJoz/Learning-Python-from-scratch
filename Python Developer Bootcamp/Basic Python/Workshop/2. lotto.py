from random import randint


def getting_number():
    while True:
        try:
            num = int(input("Enter a number: "))
            if 0 < num <= 49:
                break
            else:
                print("Entered number is out of range: 1-49. Try again.")
        except ValueError:
            print("Invalid number! Try again")
    return num


def getting_6numbers():
    numbers = []
    while len(numbers) < 6:
        number = getting_number()
        if number not in numbers:
            numbers.append(number)
        else:
            print("You have already entered this number. Try again")
    return sorted(numbers)


def lotto():
    print(getting_6numbers())


if __name__ == "__main__":
    lotto()


