from flask import Flask

app = Flask(__name__)


@app.route("/licz/<int:liczba1>/<int:liczba2>")
def add_num(liczba1, liczba2):
    total = liczba1 + liczba2
    return f"{total}"


if __name__ == "__main__":
    app.run(debug=True)
