def list_keys(d):
    for key in d:
        print(key)


def list_keys_values(d):
    for key in d:
        print(key, d[key], sep=": ")


def list_keys_values2(d):
    for key in d.items():
        print(key)


if __name__ == "__main__":
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    list_keys(d)
    print()
    list_keys_values(d)
    print()
    list_keys_values2(d)
