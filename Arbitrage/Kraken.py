from bs4 import BeautifulSoup as bs
import requests
import time
import json
def kraken(symbol):
    my_url = f"https://api.kraken.com/0/public/Ticker?pair={symbol}USD"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    headers = {"user-agent": USER_AGENT}

    response = requests.get(my_url, headers=headers,)

    data = json.loads(response.text)
    return int(float(data["result"][f"X{symbol}ZUSD"]["b"][0]))


if __name__ == "__main__" :
    kraken_price=kraken("ETH")
