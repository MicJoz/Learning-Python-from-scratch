def histogram(input_list):
    for i in input_list:
        if type(i) != int:
            return None
    else:
        display = ""
        for i in input_list:
            # if display != "": ## adds blank line between h and h1 print
            display += "\n"
            for j in range(i):
                display += "#"
    return display


if __name__ == "__main__":
    h = histogram([1, 2, 3, "r"])
    print(h)
    h1 = histogram([4, 3, 5, 2, 1])
    print(h1)

