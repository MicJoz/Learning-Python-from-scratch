def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def iterate_through(num):
    for i in range(1, num + 1):
        if is_even(i):
            print(f"{i} - even")


iterate_through(22)