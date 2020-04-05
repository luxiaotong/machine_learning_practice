import requests
from bs4 import BeautifulSoup
import pickle


def save_sp500_tickers():
    proxy = {"http": "http://127.0.0.1:1081",
             "https": "https://127.0.0.1:1081"}
    r = requests.get(
        "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies", proxies=proxy)

    soup = BeautifulSoup(r.text, 'html.parser')
    tr_list = soup.find("table", id="constituents").find_all('tr')[1:]

    tickers = []
    for tr in tr_list:
        ticker = tr.find_all("td")[0].text.rstrip()
        tickers.append(ticker)

    with open('./python_programming_for_finance/sp500tickers.pickle', 'wb') as f:
        pickle.dump(tickers, f)

    print(tickers)


save_sp500_tickers()
