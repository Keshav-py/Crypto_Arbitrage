import requests
import time
import json
def Zebpay(symbol):
    my_url = f"https://www.zebapi.com/pro/v1/market/{symbol}-INR/ticker"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
    headers = {"user-agent": USER_AGENT}

    response = requests.get(my_url, headers=headers, )

    data = json.loads(response.text)
    return int(data["sell"])


if __name__ == "__main__" :
    zebpay_price=Zebpay("ETH")

#https://www.zebapi.com/pro/v1/market/ETH-INR/ticker