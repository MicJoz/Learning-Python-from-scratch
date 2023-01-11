from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)


@app.route('/guess', methods=["GET", "POST"])
def calc():
    answer = randint(1, 100)
    if request.method == "POST":
        guess = int(request.form["guess"])
        check = ""
        if guess > answer:
            check = "Too much"
        elif guess < answer:
            check = "Not enough"
        elif guess == answer:
            check = "You have guessed. Congratulations!"
        return render_template("base9.html", msg=check)
    else:
        return render_template("base9.html")


if __name__ == "__main__":
    app.run(debug=True)
