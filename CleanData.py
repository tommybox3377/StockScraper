import pandas as pd
import datetime
import MySQL
import math

xlsx_file = r"C:\Users\twmar\OneDrive\Documents\Data\Stocks\Data.xlsx"


def timestamp_to_datetime(time):
    return time.to_pydatetime().replace(second=0, microsecond=0)


def return_next_min(time):
    return time + datetime.timedelta(minutes=1)


def check_time(time1, time2):
    if time2 - time1 == datetime.timedelta(minutes=1):
        return True
    else:
        return False



def add_all_the_minutes():
    stop_dt = datetime.datetime(year=2022, month=2, day=24, hour=10, minute=37)
    next_min = datetime.datetime(year=2019, month=10, day=21, hour=10, minute=50)

    while next_min < stop_dt:
         MySQL.my_cursor.execute(f"INSERT INTO raw_data (datetime) VALUES ('{next_min}')")
         next_min = next_min + datetime.timedelta(minutes=1)

    MySQL.mydb.commit()
    print("added minutes")


def import_from_xl_to_db():
    df1 = pd.read_excel(xlsx_file)
    df1["datetime"] = df1["datetime"].apply(lambda x: timestamp_to_datetime(x))
    print("starting")
    for i in range(0, len(df1.index)):
        s = df1.iloc[i].fillna("NULL")
        dt = s.loc["datetime"]
        gold = s.loc["Gold"]
        oil = s.loc["Crude Oil"]
        DJ = s.loc["Dow Jones"]
        SP = s.loc["S&P 500"]
        NAS = s.loc["NASDAQ"]
        gUSD = s.loc["Global USD"]
        aDJIA = s.loc["Asia DJIA"]
        n225 = s.loc["NIKKEI 225"]
        ftse = s.loc["FTSE 100"]
        e_u = s.loc["EUR/USD"]
        u_j = s.loc["USD/JPY"]
        u_c = s.loc["USD/CNY"]
        u10y = s.loc["U.S. 10 Yr. Note"]
        j10y = s.loc["JP 10 Yr Bond"]
        g10y = s.loc["Germ. 10 Yr Bond"]

        MySQL.my_cursor.execute(f"UPDATE raw_data SET Gold = {gold}, CrudeOil = {oil}, DowJones = {DJ}, SP500 = {SP}, NASDAQ = {NAS}, GlobalUSD = {gUSD}, ASIADJIA = {aDJIA}, NIKKEI225 = {n225}, FTSE100 = {ftse}, EURUSD = {e_u}, USDJPY = {u_j}, USDCNY = {u_c}, US10YRNOTE = {u10y}, JP10YRBOND = {j10y}, GER10YRBOND = {g10y} WHERE datetime = '{dt}'")
        # print(str(dt) + f"UPDATE raw_data SET Gold = {gold}, CrudeOil = {oil}, DowJones = {DJ}, SP500 = {SP}, NASDAQ = {NAS}, GlobalUSD = {gUSD}, ASIADJIA = {aDJIA}, NIKKEI225 = {n225}, FTSE100 = {ftse}, EURUSD = {e_u}, USDJPY = {u_j}, USDCNY = {u_c}, US10YRNOTE = {u10y}, JP10YRBOND = {j10y}, GER10YRBOND = {g10y} WHERE datetime = '{dt}'")
    MySQL.mydb.commit()


add_all_the_minutes()
# import_from_xl_to_db()
# MySQL.my_cursor.execute("TRUNCATE TABLE raw_data")

#TODO https://finance.yahoo.com/quote/%5ETNX/history?p=^TNX&.tsrc=fin-srch