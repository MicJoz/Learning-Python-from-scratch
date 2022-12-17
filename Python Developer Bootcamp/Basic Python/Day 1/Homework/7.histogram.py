def histogram(input_list):
    display = ""
    for item in input_list:
        if type(item) != int:
            return None
    else:
        for i in range(len(input_list)):
            if display != "":
                display += "\n"
            for j in range(input_list[i]):
                display += "#"
    return display


h = histogram([1, 2, 3, "r"])
print(h)
h1 = histogram([4, 3, 5, 2, 1])
print(h1)

