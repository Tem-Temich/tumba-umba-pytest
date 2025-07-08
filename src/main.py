def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""
    if isinstance(prices,list):
        if tax_rate < 0:
            raise ValueError('Неверный налоговый процент')

        taxed_prices = []

        for price in prices:
            if price <= 0:
                raise ValueError('Неверная цена')
            tax = price * tax_rate / 100
            taxed_prices.append(price + tax)

        return taxed_prices
    elif isinstance(prices,int):
        return prices*tax_rate*0.01+prices



def calculate_tax(price: float, tax_rate: float) -> float:
    '''
    Функция должна вычислять стоимость товара с учетом налога и возвращать результат
    '''
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError('Неверная цена')
    if not isinstance(tax_rate, (int, float)) or tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    return price * (1 + tax_rate / 100)