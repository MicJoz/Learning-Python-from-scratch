def fizz_buzz(min, max):
    min = int(input("Enter a position to start: "))
    max = int(input("Enter a position to stop: "))
    for i in range(min, max + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizz_buzz(min, max)
