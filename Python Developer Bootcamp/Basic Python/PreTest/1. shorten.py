def shorten(text):
    text_to_shorten = text[0]
    for i in range(0, len(text)):
        if text[i] == " ":
            text_to_shorten += text[i + 1]
    return text_to_shorten.upper()


text = input("Enter a string to shorten: ")
print(shorten(text))

