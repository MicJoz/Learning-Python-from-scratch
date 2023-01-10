from flask import Flask
from _datetime import datetime

app = Flask(__name__)


@app.route("/<string:current_time>")
def data(current_time):
    current_time = datetime.now()
    time = current_time.strftime("%d %B %Y %H:%M:%S")
    return f"{time}"


if __name__ == "__main__":
    app.run(debug=True)
