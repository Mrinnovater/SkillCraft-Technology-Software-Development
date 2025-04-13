from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'guess-game-shiva'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        naam = request.form['name']
        session['naam'] = naam
        session['number'] = random.randint(1, 30)
        session['guesses_took'] = 0
        session['max_guesses'] = 3
        return redirect(url_for('game'))
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    naam = session['naam']
    max_guesses = session['max_guesses']
    number = session['number']
    guesses_took = session['guesses_took']
    message = ""
    remaining = max_guesses - guesses_took

    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['guesses_took'] += 1
        guesses_took = session['guesses_took']
        remaining = max_guesses - guesses_took

        if guess == number:
            return render_template("result.html", message="BOOYAH!!! You Nailed it 🎉", detail=f"Nice Job, {naam}. You took {guesses_took} guesses.")
        elif guesses_took == max_guesses:
            return render_template("result.html", message="OOPS! Out of Chances 😢", detail=f"Well Tried, {naam}. The number was {number}.")
        else:
            message = f"OOPS!!! Incorrect Guess {guess}. You have {remaining} chances left."

    return render_template("game.html", naam=naam, message=message, remaining=remaining)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
