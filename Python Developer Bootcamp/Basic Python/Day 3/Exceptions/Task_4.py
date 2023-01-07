numbers = [600600600, 500500500]


def phone(number):
    try:
        if number in numbers:
            return number
        else:
            raise Exception("Nie ma takiego numeru")
    except Exception as error:
        return error


if __name__ == "__main__":
    print(phone(500500501))
    print(phone(500500500))
