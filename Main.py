from datetime import datetime, timedelta
import mysql.connector
import requests
from bs4 import BeautifulSoup as bs

dt = datetime.now()

mydb = mysql.connector.connect(
    host="host.adress",
    user="user",
    password="password",
    database="stockdata"
)

my_cursor = mydb.cursor()

future_url_base = "https://www.marketwatch.com/investing/future/"
index_url_base = "https://www.marketwatch.com/investing/index/"
currency_url_base = "https://www.marketwatch.com/investing/currency/"
bond_url_base = "https://www.marketwatch.com/investing/bond/"

futures = [
    "gold",
    "crude%20oil%20-%20electronic"
]

indexes = [
    "djia",
    "spx",
    "comp",
    "gdow",
    "adow?countrycode=xx",
    "/nik?countrycode=jp",
    "ukx?countrycode=uk"
]

currencies = [
    "eurusd",
    "usdjpy",
    "usdcny",
]

bonds = [
    "tmubmusd10y?countrycode=bx",
    "tmbmkjp-10y?countrycode=bx",
    "tmbmkde-10y?countrycode=bx",
]


def timestamp_to_datetime(time):
    return time.replace(second=0, microsecond=0)


def url_builder():
    urls = []
    for future in futures:
        urls.append(future_url_base + future)
    for index in indexes:
        urls.append(index_url_base + index)
    for currency in currencies:
        urls.append(currency_url_base + currency)
    for bond in bonds:
        urls.append(bond_url_base + bond)
    return urls


urls = url_builder()

for i, url in enumerate(urls):
    data = bs(requests.get(url).text, "html.parser").find("meta", {"name": "price"})["content"].replace(",", "")
    if "gold" in url:
        gold = data
    elif "crude%20oil%20-%20electronic" in url:
        oil = data
    elif "djia" in url:
        DJ = data
    elif "spx" in url:
        SP = data
    elif "comp" in url:
        NAS = data
    elif "gdow" in url:
        gUSD = data
    elif "adow?countrycode=xx" in url:
        aDJIA = data
    elif "/nik?countrycode=jp" in url:
        n225 = data
    elif "ukx?countrycode=uk" in url:
        ftse = data
    elif "eurusd" in url:
        e_u = data
    elif "usdjpy" in url:
        u_j = data
    elif "usdcny" in url:
        u_c = data
    elif "tmubmusd10y?countrycode=bx" in url:
        u10y = data
    elif "tmbmkjp-10y?countrycode=bx" in url:
        j10y = data
    elif "tmbmkde-10y?countrycode=bx" in url:
        g10y = data


if datetime.now() - dt < timedelta(seconds=50):
    my_cursor.execute(f"UPDATE raw_data SET Gold = {gold}, CrudeOil = {oil}, DowJones = {DJ}, SP500 = {SP}, NASDAQ = {NAS}, GlobalUSD = {gUSD}, ASIADJIA = {aDJIA}, NIKKEI225 = {n225}, FTSE100 = {ftse}, EURUSD = {e_u}, USDJPY = {u_j}, USDCNY = {u_c}, US10YRNOTE = {u10y}, JP10YRBOND = {j10y}, GER10YRBOND = {g10y} WHERE datetime = '{timestamp_to_datetime(dt)}'")
    mydb.commit()