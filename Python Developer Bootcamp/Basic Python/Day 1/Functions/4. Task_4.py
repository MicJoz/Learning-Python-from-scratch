def convert_to_usd(zlotys):
    usd = zlotys / 3.85
    return round(usd, 2)


if __name__ == "__main__":
    print(f"{convert_to_usd(100)} $")
