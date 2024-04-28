#!/usr/bin/python3
"""RUN AN APP with flask"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function that return Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbhb():
    """ Function that returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """Function that returns about c"""
    message = text.replace('_', ' ')
    return f"C {message}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_py(text="is cool"):
    """Function that returns about python"""
    message = text.replace('_', ' ')
    return f"Python {message}"


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """Function that takes n only intger"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """Function that takes n only intger"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """Function that takes n check even or odd"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
