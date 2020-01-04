#AUTHOR: Kshitij Nath
from bs4 import BeautifulSoup
import requests

url = 'https://www.compareremit.com/'
res = requests.get(url)
print(res)
bs=BeautifulSoup(res.text,'html.parser')
print(bs.title.string)

rate = list(bs.select('.exchange-rate')[0].children)[3].getText()
rate_inr=rate.split()[3]
print(type(rate_inr))
rate_inr=float(rate_inr)

def exchange(value):
    return value/rate_inr

