import logging
from binance.exceptions import BinanceAPIException
from binance.client import Client
from dotenv import load_dotenv
from bot.loging_config import loggings
import os
load_dotenv()
loggings()



def get_client():
    try:
        logging.info('Creating the client')
        API_KEY = os.getenv('API_KEY')
        API_SECRET = os.getenv('API_SECRET')
        client = Client(api_key =API_KEY,
                    api_secret=API_SECRET,
                    demo=True)
        return client
    except BinanceAPIException as e:
        logging.error('Can not login',{e})
    except Exception:
        raise('Error in extablishing client',{Exception})

if __name__ =='__main__':
    get_client()