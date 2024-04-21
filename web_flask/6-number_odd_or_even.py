#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """Displays 'C ' followed by the value of the text"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text="is cool"):
    """Displays 'Python ' followed by the value of the text variable"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Displays 'n is a number' only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Displays a HTML page if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    """Displays a HTML page if n is an integer"""
    if n % 2 == 0:
        o_or_e = "even"
    else:
        o_or_e = "odd"
    return render_template('6-number_odd_or_even.html', n=n, o_or_e=o_or_e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)