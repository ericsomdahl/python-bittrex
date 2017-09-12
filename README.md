python-bittrex  
==============

[![Build Status](https://travis-ci.org/ericsomdahl/python-bittrex.svg?branch=travis-setup)](https://travis-ci.org/ericsomdahl/python-bittrex)

Python bindings for bittrex.  I am Not associated -- use at your own risk, etc.

Tips are appreciated:
* BTC: 1D7F9ZF6BCoCh2MncK15jxHM1T5BPX9Ajd
* LTC: LaasG9TRa9p32noN2oKUVVqrDFp4Ja1NK3


Example Usage
-------------

```python
from bittrex import Bittrex

my_bittrex = Bittrex(None, None)
my_bittrex.get_markets()
{'success': True, 'message': '', 'result': [{'MarketCurrency': 'LTC', ...
```

To access account methods, an API key for your account is required and can be 
generated on the `Settings` then `API Keys` page. 
Make sure you save the secret, as it will not be visible 
after navigating away from the page. 

```python
from bittrex import Bittrex

my_bittrex = Bittrex("<my_api_key>", "<my_api_secret>")

my_bittrex.get_balance('ETH')
{'success': True, 
 'message': '',
 'result': {'Currency': 'ETH', 'Balance': 0.0, 'Available': 0.0, 
            'Pending': 0.0, 'CryptoAddress': None}
}
```


Testing
-------


In order to run the integration tests, a file called "secrets.json" must be added to the test folder.
Structure it as follows, adding your API keys:

```json
{
  "key": "mykey",
  "secret": "mysecret"
}
```
