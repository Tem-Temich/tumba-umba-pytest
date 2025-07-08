from src.main import calculate_taxes
import pytest

@pytest.mark.parametrize('price,tax,expected', [
    ([10,20,30,40], 10, [11.0, 22.0, 33.0, 44.0]),
    ([10],10,[11]),
    ([100],100,[200]),
    (100,10,110),
    (100,0,100),
    (0,0,0)
])
def test_calculate_taxes(price,tax,expected):
    assert calculate_taxes(price,tax) == expected

def test_negative_price():
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([-100], 10)
    assert str(exc_info.value) == 'Неверная цена'

def test_negative_tax():
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([100], -10)
    assert str(exc_info.value) == 'Неверный налоговый процент'