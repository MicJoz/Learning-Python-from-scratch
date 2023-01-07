def safe_get(input_list, num):
    try:
        output = input_list[num]
        return output
    except IndexError:
        return None


if __name__ == "__main__":
    print(safe_get([1, 2, 3, 4, 5], 1))
    print(safe_get([1, 2, 3, 4, 5], 5))
