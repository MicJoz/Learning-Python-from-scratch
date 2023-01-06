def find_boundaries(input_list):
    if not input_list:
        return None

    temp_output = [item for item in input_list if type(item) == int or type(item) == float]

    output = (min(temp_output), max(temp_output))
    return output


if __name__ == "__main__":
    print(find_boundaries([10, 50.5, 4, "zonk"]))
    print()
    print(find_boundaries([10, 6, 4, -1]))
    print()
    print(find_boundaries([]))
