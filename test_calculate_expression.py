from services import calculate_expression

# Тест для функции calculate_expression
def test_calculate_expression():
    result = calculate_expression("1 + 2")
    assert result == 3

def test_calculate_expression_error():
    result = calculate_expression("1 + 2 )")
    assert result == "Ошибка: unmatched ')'"
