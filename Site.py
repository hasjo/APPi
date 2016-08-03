'''This is my Pi API Website!'''
from flask import Flask, render_template
import os
from mpmath import *
from decimal import *
APP = Flask(__name__)

@APP.route('/')
def index():
    '''Returns info stuff'''
    return('curl this site /number to get number digits of pi, ex: site/4 will get 3.142')


@APP.route('/<number>')
def calc(number):
    '''Generates the pi'''
    try:
        dignum = int(number)
    except ValueError:
        return "THATS NOT A WHOLE NUMBER - TRY AGAIN"
    mp.dps = dignum
    return str(+pi)

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=8080)
