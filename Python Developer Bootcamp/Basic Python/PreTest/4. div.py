def div(min, max):
    min = int(input("Enter a position to start: "))
    max = int(input("Enter a position to stop: "))
    div_list = []
    for i in range(min, max + 1):
        if i % 2 == 0 and not i % 3 == 0:
            div_list.append(i)
    return div_list


print(div(min, max))
