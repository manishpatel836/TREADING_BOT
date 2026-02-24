import logging

def loggings():
    logging.basicConfig(filename='bot.log',
                        level=logging.INFO,
                        format='%(asctime)s-%(message)s')