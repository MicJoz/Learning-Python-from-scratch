def name_sorter(names):
    males = []
    females = []
    for item in names:
        if item.endswith("a"):
            females.append(item)
        else:
            males.append(item)
    output = {
        "female": sorted(females),
        "male": sorted(males)
    }
    return output


if __name__ == "__main__":
    input_data = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
    print(name_sorter(input_data))
