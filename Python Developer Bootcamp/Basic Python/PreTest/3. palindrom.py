def check_palindrome(text):
    temp = text.lower()
    temp = temp.split()
    text_to_check = "".join(temp)
    # if text_to_check == text_to_check[::-1]:
    #     return True
    # else:
    #     return False
    return text_to_check == text_to_check[::-1]


if __name__ == "__main__":
    str_to_check = input("Enter text: ")
    print(check_palindrome(str_to_check))
