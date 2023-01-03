def check_palindrome(text):
    text = text.lower()
    text_no_spaces = ""
    for i in text:
        if i == " ":
            continue
        else:
            text_no_spaces += i

    if text_no_spaces == text_no_spaces[::-1]:
        return True
    else:
        return False


str_to_check = input("Enter text: ")
print(check_palindrome(str_to_check))
