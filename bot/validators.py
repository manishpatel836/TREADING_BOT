def symbol_validation(symbol)->str:
    if not isinstance(symbol,str):
        raise ValueError('Symbol must be valid string')
    symbol = symbol.upper().strip()
    if not symbol.isalnum():
        raise ValueError('Symbols contains numerical character')
    return symbol

def price_validation(price)->float:
    if not isinstance(price,(float,int)):
        raise ValueError('Price must be in 0.00 or 00 format')
    price = float(price)
    if price <= 0:
        raise ValueError('Price can not be negative')
    return price

def quantity_validation(quantity)->float:
    if not isinstance(quantity,(float,int)):
        raise ValueError('quantity must be in 0.00 or 00 format')
    quantity = float(quantity)
    if quantity <= 0:
        raise ValueError('quantity can not be negative')
    return quantity

def side_validator(side)->str:
    if side not in ['BUY','SELL']:
        raise('side must be buy or sell')
    