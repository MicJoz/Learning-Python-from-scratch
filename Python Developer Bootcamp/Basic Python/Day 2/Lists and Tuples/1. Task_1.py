def create_list(arg_1, arg_2):
    quadruple_list = []
    for i in range(4):
        quadruple_list.append(arg_1)
        quadruple_list.append(arg_2)
    return quadruple_list


if __name__ == "__main__":
    print(create_list(123, 456))
    print(create_list(True, False))
    