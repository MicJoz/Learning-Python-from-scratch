def divide(a, b):
    try:
        if a >= 0:
            if b >= 0:
                try:
                    output = a / b
                    return output
                except ZeroDivisionError:
                    return None
    except:
        pass
    else:
        return None


if __name__ == "__main__":
    print(divide(6, 3))
    print(divide(6, -3))
    print(divide(6, 0))
