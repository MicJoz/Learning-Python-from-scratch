def div():
    while True:
        try:
            num1 = abs(int(input("Enter first number: ")))
            num2 = abs(int(input("Enter second number: ")))
            output = num1 / num2
            break
        except ValueError:
            print("Invalid number! Try again")
        except ZeroDivisionError:
            print("Second number must not be 0")
    return output


if __name__ == "__main__":
    print(div())
