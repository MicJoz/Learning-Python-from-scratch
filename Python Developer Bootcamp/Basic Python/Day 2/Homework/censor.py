def censor(input_string):
    not_allowed_words = ["Java", "C#", "Ruby", "PHP"]
    censorship = "****"
    words_to_check = input_string.split()
    censored_words = []
    for word in words_to_check:
        if word in not_allowed_words:
            censored_words.append(censorship)
        else:
            censored_words.append(word)
    output = " ".join(censored_words)
    return output


if __name__ == "__main__":
    c = censor("Java is the best, but PHP is the bestest!")
    print(c)
    d = censor("Lorem ipsum dolor sit amet, consectetur adipiscing")
    print(d)
