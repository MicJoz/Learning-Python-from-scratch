def format_date(day, month, year):
    months = {
        1: "stycznia",
        2: "lutego",
        3: "marca",
        4: "kwietnia",
        5: "maja",
        6: "czerwca",
        7: "lipca",
        8: "sierpnia",
        9: "września",
        10: "października",
        11: "listopada",
        12: "grudnia"
    }
    days = {
        "stycznia": 31,
        "lutego": 28,
        "marca": 31,
        "kwietnia": 30,
        "maja": 31,
        "czerwca": 30,
        "lipca": 31,
        "sierpnia": 31,
        "września": 30,
        "października": 31,
        "listopada": 30,
        "grudnia": 31
    }

    if month not in months:
        return None

    month_to_check = months[month]
    if day > days[month_to_check]:
        return None

    output = f"{day} {months[month]} {year}"
    return output


if __name__ == "__main__":
    print(format_date(28, 2, 2020))
    print(format_date(33, 12, 2020))
