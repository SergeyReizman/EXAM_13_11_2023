# tools/numbers/comp.py

def check_simp_module():
    pass  # This function will be defined in main.py

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]
