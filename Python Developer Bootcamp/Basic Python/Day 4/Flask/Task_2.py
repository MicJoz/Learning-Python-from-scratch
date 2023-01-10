from flask import Flask
from _datetime import datetime

app = Flask(__name__)


@app.route("/<string:current_time>")
def time(current_time):
    current_time = (datetime.now()).strftime("%H:%M:%S")
    return f"{current_time}"


if __name__ == "__main__":
    app.run(debug=True)
