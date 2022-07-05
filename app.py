from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/', methods = ['GET', "POST"])
def guess():
    counter = 0
    message = ""
    if request.method == 'POST':
        counter += 1
        form = request.form
        user_guess = int(form["guess"])
        comp_num = random.randint(1, 10)

        if comp_num == user_guess:
            message = "Well done, you got it"
            return render_template("game_over.html", message=message)
        elif comp_num > user_guess:
            message = "Too low"
        else:
            message = "Too high"
            if counter == 3:
                message = "You failed"
                return render_template("game_over.html", message=message)
    return render_template("base.html", message=message)


if __name__ == '__main__':
    app.run(debug=True)
