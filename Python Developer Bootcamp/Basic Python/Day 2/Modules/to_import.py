import random

words = ["hello", "darkness", "my", "old", "friend"]


def random_words():
    word = random.choice(words)
    return word


def welcome():
    return "Welcome!"
