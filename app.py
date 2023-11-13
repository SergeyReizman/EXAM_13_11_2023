# app.py
from flask import Flask, render_template
from tools.numbers import simp, comp
import cal  # Import the cal module directly
import os  # Import the os module

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    # Use functions from simp and comp modules
    result_add = simp.add(5, 3)
    result_subtract = simp.subtract(8, 2)
    result_sum_digits = comp.sum_of_digits(123)
    result_is_palindrome = comp.is_palindrome(121)
    
    # Import myzip function from cal module
    result_zip = cal.myzip([1, 2, 3], ['a', 'b', 'c'])

    return render_template('index.html',
                           result_add=result_add,
                           result_subtract=result_subtract,
                           result_sum_digits=result_sum_digits,
                           result_is_palindrome=result_is_palindrome,
                           result_zip=list(result_zip))

if __name__ == '__main__':
    app.run(debug=True)
