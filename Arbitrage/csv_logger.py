import csv
from Kraken import kraken
from zebpay import Zebpay
from usd_to_inr import usd_to_inr
import time
from datetime import datetime


while True:
    now = datetime.now()
    zebpay_price=Zebpay("ETH")
    kraken_price=kraken("ETH")
    Usd_Price=usd_to_inr()

    time.sleep(5)

    kraken_price_inr=kraken_price * Usd_Price

    profitAmt= zebpay_price - kraken_price_inr

    profit_Percentage=(profitAmt/kraken_price_inr)*100

    #print(kraken_price_inr,"%.2f" % profit_Percentage,profitAmt)

    current_time = now.strftime("%d/%m/%Y")
    current_date = now.strftime("%H:%M:%S")

    rows=[current_date,current_time,kraken_price_inr,zebpay_price,profitAmt,"%.2f" % profit_Percentage]

    filename="Arbitrage.csv"

    with open(filename, "a") as csvfile:

        writer=csv.writer(csvfile)
        writer.writerow(rows)

    time.sleep(600)