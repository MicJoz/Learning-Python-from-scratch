from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/lotek")
def lotto():
    numbers = []
    while len(numbers) < 6:
        number = randint(1, 49)
        if number not in numbers:
            numbers.append(number)
    num1, num2, num3, num4, num5, num6 = sorted(numbers)
    return f"Wylosowane liczby to: {num1}, {num2}, {num3}, {num4}, {num5}, {num6}."


if __name__ == "__main__":
    app.run(debug=True)
