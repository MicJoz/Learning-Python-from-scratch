def pesel(str_to_check):
    char11 = [letter for letter in str_to_check]
    factors = {
        1: 1,
        2: 3,
        3: 7,
        4: 9,
        5: 1,
        6: 3,
        7: 7,
        8: 9,
        9: 1,
        10: 3
    }
    total10 = 0
    i = 1
    for item in char11[0:-1]:
        total10 += int(item) * factors[i]
        i += 1
    modulo10 = total10 % 10
    if modulo10 == 10:
        modulo10 = 10
    num_to_check = 10 - modulo10
    if num_to_check == int(char11[-1]):
        return True
    else:
        return False


if __name__ == "__main__":
    print(pesel("44051401358"))
    print(pesel("96051323731"))
