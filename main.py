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

    # create limit buy order
    try:
        #create buy market order
        order = exchange.create_market_buy_order(data['symbol'], data['quantity'])
        # order = exchange.create_limit_buy_order(data['symbol'], data['amount'], data['price'])
    except Exception as e:
        return {'ERROR': str(e)}
    return order