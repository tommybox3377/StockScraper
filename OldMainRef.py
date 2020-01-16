from datetime import datetime, timedelta
import re
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("Creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Data").sheet1
date_times = sheet.col_values(1)

write_row = len(date_times) + 1

date_check = datetime.strptime(sheet.cell(write_row - 1, 1).value, "%m/%d/%Y %H:%M:%S")

now = datetime.now()

if (now - date_check) > timedelta(seconds=30):
    sheet.update_cell(write_row, 1, str(now))
    for i, url in enumerate(urls):
        response = requests.get(urls[i])
        m = re.search(r"\"price\" content=\"(.*)\">", response.text)
        value = float(m.group(1).replace(",", ""))
        sheet.update_cell(write_row, i + 2, value)
