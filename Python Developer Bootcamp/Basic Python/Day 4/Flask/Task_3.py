from flask import Flask
from _datetime import datetime

app = Flask(__name__)


@app.route("/<string:current_date>")
def date(current_date):
    current_date = (datetime.now()).strftime("%d %B %Y")
    return f"{current_date}"


if __name__ == "__main__":
    app.run(debug=True)
