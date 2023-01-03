def find_first_and_last(input_list):
    output = (input_list[0], input_list[-1])
    return output


if __name__ == "__main__":
    print(find_first_and_last([10, 9, 8, 15]))
