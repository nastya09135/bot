import pytest
from services import get_random

# Тесты для функции get_random
def test_get_random_within_range():
    result = get_random(1, 6)
    assert 1 <= result <= 6
        
def test_get_random_default_range():
    result = get_random()
    assert 1 <= result <= 6

def test_get_random_custom_range():
    result = get_random(10, 15)
    assert 10 <= result <= 15

def test_get_random_invalid_range():
    with pytest.raises(ValueError):
        get_random(6, 1)

