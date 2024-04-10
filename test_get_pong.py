from services import get_pong

# Тест для функции get_pong
def test_get_pong_output():
    result = get_pong()
    assert result == "pong"
    