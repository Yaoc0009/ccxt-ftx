import ccxt
import config

creds = config.CREDENTIALS

# get the ftx exchange instance
exchange_id = 'ftx'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': creds['api_key'],
    'secret': creds['secret'],
    "headers": {
        "FTX-SUBACCOUNT": creds['account']
    }
})

# create function to get quote via request
def get_quote(request):
    symbol = request.args.get('symbol')
    
    try:
        # get the quote of the currency
        quote = exchange.fetch_ticker(symbol)
    except Exception as e:
        return {'ERROR': str(e)}
    
    return quote

# create function to create order via single json request
def trade_crypto(request):
    data = request.get_json()

    try:
        #create buy market order
        order = exchange.create_order(data['symbol'], data['type'], data['side'], data['amount'], data['price'], data['params'])
    except Exception as e:
        return {'ERROR': str(e)}
    return order

print(dir(ccxt.exchange()))           # Python

########################## CREATE ORDERS ##########################

# def create_limit_order(self, symbol, side, amount, price, params={}) -> dict:
#     return self.create_order(symbol, 'limit', side, amount, price, params)

# def create_market_order(self, symbol, side, amount, price=None, params={}) -> dict:
#     return self.create_order(symbol, 'market', side, amount, price, params)

# def create_limit_buy_order(self, symbol, amount, price, params={}) -> dict:
#     return self.create_order(symbol, 'limit', 'buy', amount, price, params)

# def create_limit_sell_order(self, symbol, amount, price, params={}) -> dict:
#     return self.create_order(symbol, 'limit', 'sell', amount, price, params)

# def create_market_buy_order(self, symbol, amount, params={}) -> dict:
#     return self.create_order(symbol, 'market', 'buy', amount, None, params)

# def create_market_sell_order(self, symbol, amount, params={}) -> dict:
#     return self.create_order(symbol, 'market', 'sell', amount, None, params)


########################## EDIT ORDERS ##########################

# def edit_limit_buy_order(self, id, symbol, *args):
#     return self.edit_limit_order(id, symbol, 'buy', *args)

# def edit_limit_sell_order(self, id, symbol, *args):
#     return self.edit_limit_order(id, symbol, 'sell', *args)

# def edit_limit_order(self, id, symbol, *args):
#     return self.edit_order(id, symbol, 'limit', *args)

# def edit_order(self, id, symbol, *args):
#     if not self.enableRateLimit:
#         raise ExchangeError('edit_order() requires enableRateLimit = true')
#     self.cancel_order(id, symbol)
#     return self.create_order(symbol, *args)