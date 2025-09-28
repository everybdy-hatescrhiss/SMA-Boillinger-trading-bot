import MetaTrader5 as mt5
from time import sleep

from projects.atj_trading_legacy.mt5_trade_utils import send_market_order, close_all_positions
from config import mt5_credentials

if __name__ == '__main__':
    
    mt5.initialize(mt5_credentials['exe_path'])

   
    login = mt5_credentials['login']
    password = mt5_credentials['password']
    server = mt5_credentials['server']

    mt5.login(login, password, server)

  
    sleep(5)
    res = send_market_order('US30', 1.0, 'buy', magic=10)

  
    sleep(5)
    send_market_order('XAUUSD', 1.0, 'buy', magic=20)

 
    sleep(5)

    close_all_positions('all', magic=10)

 
    sleep(5)
    close_all_positions('all', magic=20)