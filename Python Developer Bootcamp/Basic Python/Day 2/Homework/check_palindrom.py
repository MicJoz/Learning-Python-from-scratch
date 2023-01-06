def check_palindrome(word_to_check):
    word = word_to_check.lower()
    if word == word[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    word_to_check = input("Enter a word to check: ")
    print(check_palindrome(word_to_check))
