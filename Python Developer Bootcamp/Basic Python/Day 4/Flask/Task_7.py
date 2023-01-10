from flask import Flask, request
from random import randint

app = Flask(__name__)


@app.route("/name", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = request.form["user_name"]
        # user_surname = request.form["user_surname"]
        return f"Hello {user_name}"
    else:
        return '''<form action='/name', method='POST'>
                           <label>
                               Name:
                               <input type="text" name="user_name">
                           </label>
                           <label>
                               <button type="submit">
                                   Send
                               </button>
                           </label>
                    </form>
                '''


if __name__ == "__main__":
    app.run(debug=True)
