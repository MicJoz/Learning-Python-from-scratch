from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/losuj")
def draw_num():
    numbers = []
    for i in range(0, 3):
        numbers.append(randint(1, 100))
    num1, num2, num3 = sorted(numbers)
    return f"Wylosowane liczby to: {num1}, {num2}, {num3}"


if __name__ == "__main__":
    app.run(debug=True)
