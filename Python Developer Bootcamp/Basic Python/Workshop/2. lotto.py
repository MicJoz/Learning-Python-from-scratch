from random import randint


def getting_user_number():
    while True:
        try:
            user_number = int(input("Enter a number: "))
            if 0 < user_number <= 49:
                break
            else:
                print("Entered number is out of range: 1 - 49. Try again.")
        except ValueError:
            print("Invalid number! Try again")
    return user_number


def getting_user_numbers():
    numbers = []
    while len(numbers) < 6:
        number = getting_user_number()
        if number not in numbers:
            numbers.append(number)
        else:
            print("You have already entered this number. Try again.")
    return sorted(numbers)


def printing_user_numbers(user):
    user_numbers = ""
    for number in user:
        user_numbers += str(number) + ", "
    return user_numbers[0:-2]


def getting_comp_numbers():
    comp_random_numbers = []
    while len(comp_random_numbers) < 6:
        temp = randint(1, 49)
        if temp not in comp_random_numbers:
            comp_random_numbers.append(temp)
    return sorted(comp_random_numbers)


def printing_comp_numbers(comp):
    comp_numbers = ""
    for number in comp:
        comp_numbers += str(number) + ", "
    return comp_numbers[0:-2]


def compairing_numbers(user, comp):
    hits = 0
    for number in user:
        if number in comp:
            hits += 1
    return hits


def lotto():
    user = getting_user_numbers()
    print(f"\nYour numbers are: {printing_user_numbers(user)}.")
    comp = getting_comp_numbers()
    print(f"\nComputer numbers are: {printing_comp_numbers(comp)}.")
    print(f"\nTotal hits: {compairing_numbers(user, comp)}")


if __name__ == "__main__":
    lotto()
