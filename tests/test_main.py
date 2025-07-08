from src.main import calculate_taxes, calculate_tax

import pytest

@pytest.mark.parametrize('prices,taxs,expected', [
    ([10,20,30,40], 10, [11.0, 22.0, 33.0, 44.0]),
    ([10],10,[11]),
    ([100],100,[200]),
    (100,10,110),
    (100,0,100),
    (0,0,0)
])
def test_calculate_taxes(prices,taxs,expected):
    assert calculate_taxes(prices,taxs) == expected

def test_negative_prices():
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([-100], 10)
    assert str(exc_info.value) == 'Неверная цена'

def test_negative_taxes():
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([100], -10)
    assert str(exc_info.value) == 'Неверный налоговый процент'

@pytest.mark.parametrize('price,tax,expected',[
    (1000,1,1010),
    (200,20,240),
    (10,10,11),
    (100,0,100),
    (0,100,0)
])
def test_calculate_tax(price,tax,expected):
    assert calculate_tax(price,tax) == expected
def test_negative_price():
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(-100, 10)
    assert str(exc_info.value) == 'Неверная цена'
def test_negative_tax():
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(100, -10)
    assert str(exc_info.value) == 'Неверный налоговый процент'
