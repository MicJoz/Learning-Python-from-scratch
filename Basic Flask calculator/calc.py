from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        operation = request.form["operation"]
        if operation == "Addition":
            return str(num1 + num2)
        elif operation == "Subtraction":
            return str(num1 - num2)
        elif operation == "Multiplication":
            return str(num1 * num2)
        elif operation == "Division":
            return f"num1 / num2"
    else:
        return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
