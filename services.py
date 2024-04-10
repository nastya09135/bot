import random
import re

def is_valid_expression(expression):
    pattern = re.compile(r"[^\d\.\+\-\*\/\(\) ]")
    return not bool(pattern.search(expression))

def calculate_expression(expression):
    if not is_valid_expression(expression):
        return "Недопустимый символ в математическом выражении."
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Ошибка: {e.args[0]}"

def get_random(start = 1, end = 6):
    return random.randint(start , end)

def get_pong():
    return "pong"

def get_sum(a: int , b: int):
    return a + b
