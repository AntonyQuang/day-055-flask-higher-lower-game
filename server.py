from flask import Flask
from random import randint

random_number = randint(0, 9)

app = Flask(__name__)



@app.route('/')
def home():
    return '<h1 style="color:crimson">Guess a number between 0 and 9</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:guess>')
def correct_guess(guess):
    if guess > random_number:
        return '<h1 style="color:teal">You guessed too high!</h1>' \
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif guess < random_number:
        return '<h1 style="color:maroon">You guessed too low!</h1>' \
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style="color:blue">You got it right!</h1>' \
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

#
# if guess < random_number:
#     return "too low"
#
# of guess > random_number:
#     return "too high"

if __name__ == "__main__":
    app.run(debug=True)
