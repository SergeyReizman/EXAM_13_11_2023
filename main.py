# main.py

# Import functions from simp module
from tools.numbers import simp

# Now you can use functions from comp module
from tools.numbers import comp

# Use simp functions
result_add = simp.add(5, 3)
result_subtract = simp.subtract(8, 2)

# Use comp functions
result_sum_digits = comp.sum_of_digits(123)
result_is_palindrome = comp.is_palindrome(121)

# Import myzip function from cal module
from cal import myzip

# Use cal function
result_zip = myzip([1, 2, 3], ['a', 'b', 'c'])

# Print results
print("Result of add:", result_add)
print("Result of subtract:", result_subtract)
print("Result of sum_of_digits:", result_sum_digits)
print("Result of is_palindrome:", result_is_palindrome)
print("Result of myzip:", list(result_zip))
