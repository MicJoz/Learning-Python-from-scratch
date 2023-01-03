def make_tuple(a, b, c=3, d=4):
    new_tuple = (a, b, c, d)
    return new_tuple


if __name__ == "__main__":
    a = make_tuple("mama", "tata")
    print(a)
    b = make_tuple(0, 0, 0, 0)
    print(b)