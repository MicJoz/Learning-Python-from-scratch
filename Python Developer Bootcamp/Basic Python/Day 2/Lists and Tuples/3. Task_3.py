def find_short_words(input_list):
    short_word_list = []
    for i in input_list:
        if len(i) < 5:
            short_word_list.append(i)
    return short_word_list


if __name__ == "__main__":
    print(find_short_words(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie']))
