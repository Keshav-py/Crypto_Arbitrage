from bs4 import BeautifulSoup as bs
import requests
import time
import json
def usd_to_inr():
    my_url = "https://www.google.com/search?q=current+usd+price&rlz=1C5CHFA_enIN767IN767&oq=current+usd+price"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    headers = {"user-agent": USER_AGENT}

    response = requests.get(my_url, headers=headers,)

    soup = bs(response.content, "html.parser")

    data = soup.find("span", {"class": "DFlfde SwHCTb"}).text

    return int(float(data))





if __name__ == "__main__" :
    Usd_Price=usd_to_inr()