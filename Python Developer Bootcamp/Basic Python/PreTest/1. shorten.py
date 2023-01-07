def shorten(text):
    text_to_shorten = text.split()
    output = ""
    for item in text_to_shorten:
        output += item[0].upper()
    return output


if __name__ == "__main__":
    str_to_shorten = input("Enter a string to shorten: ")
    print(shorten(str_to_shorten))

