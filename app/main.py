#!/usr/bin/env python3

''' Simple example of Reflective Cross-Site Scripting (XSS).
    The web page asks the user's name and responds with a greeting.
    The input is not-sanitized and the output is not escaped.

    The following can be entered into the name field to demonstrate
    the xss vulnerability:

    <script>alert('xss')</script>
'''
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    '''Display a simple web page that asks the user their name
       and responds with an appropriate greeting.
    '''
    # Display the HTML form
    response = '<!DOCTYPE html>' \
               '<html><body>What is your name?' \
               '<form>' \
               '<input type="text" name="name"><br>' \
               '<input type="submit" value="Submit">' \
               '</form>' \
               '</body></html>'

    # Get the name for the parameters
    name = request.values.get('name')

    # If the name was passed, return a greeting
    if name:
        response = '<!DOCTYPE html><HTML><BODY>Hello, ' + \
                   name + '!</BODY></HTML>'

    return response
