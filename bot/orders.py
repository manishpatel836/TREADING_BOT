import logging
from bot.loging_config import loggings
from binance.exceptions import(BinanceOrderException,
                               BinanceAPIException)
loggings()
def place_market_order(client,symbol:str,side:str,type:str,quantity:float):
    try:
        logging.info(f"request:placing Spot {side} {type} Order for {quantity} {symbol}")
        order = client.create_order(
            symbol = symbol,
            type = type,
            side = side,
            quantity=quantity,
        )
        order_id = order.get('orderID')
        status = order.get('status')
        excecutedQut = order.get('executedQty')
        logging.info(f'Order ID {order_id},Status ,')
        print(f'Order ID {order_id},Status{status},excecutedQut{excecutedQut}')
        return order

    except (BinanceAPIException or BinanceOrderException) as e:
        logging.error(f'Order failed {e}')
        print(f'{e}')
    
    except Exception as e:
        logging.error(f'order failed {e}')
        print(f'{e}')

def place_limit_order(client,symbol:str,side:str,type:str,quantity:float,price:float):
    try:
        logging.info(f"request:placing Spot {side} Limit Order for {quantity} {symbol} at {price}")
        order = client.create_order(
            symbol = symbol,
            timeInForce='GTC',
            price=price,
            type = type,
            side = side,
            quantity=quantity,
        )
        order_id = order.get('orderID')
        status = order.get('status')
        excecutedQut = order.get('executedQty')
        logging.info(f'Order ID {order_id},Status{status},excecutedQut{excecutedQut}')
        print(f'Order ID {order_id},Status{status},excecutedQut{excecutedQut}')
        return order

    except (BinanceAPIException or BinanceOrderException) as e:
        logging.error(f'Order failed {e}')
        print(f'{e}')
    
    except Exception as e:
        logging.error(f'order failed {e}')
        print(f'{e}')