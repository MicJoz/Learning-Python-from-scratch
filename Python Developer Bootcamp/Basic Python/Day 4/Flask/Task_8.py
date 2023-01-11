from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        operation = request.form["operation"]
        if operation == "addition":
            return str(num1 + num2)
        elif operation == "subtraction":
            return str(num1 - num2)
        elif operation == "multiplication":
            return str(num1 * num2)
        elif operation == "division":
            return str(num1 / num2)
    else:
        return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
