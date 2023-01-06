def div(min, max):
    # div_list = []
    # for i in range(min, max + 1):
    #    if i % 2 == 0 and not i % 3 == 0:
    #        div_list.append(i)
    div_list = [i for i in range(min, max + 1) if i % 2 == 0 and not i % 3 == 0]  # list comprehension added
    return div_list


if __name__ == '__main__':
    min = int(input("Enter a position to start: "))
    max = int(input("Enter a position to stop: "))
    print(div(min, max))
