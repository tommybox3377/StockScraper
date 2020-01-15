import datetime
import mysql.connector
import Creds

mydb = mysql.connector.connect(
    # connects to MySQL
    host=Creds.host,
    user=Creds.user,
    password=Creds.password,
    database=Creds.database
)

my_cursor = mydb.cursor()
 #TODO make check when data range is just about to bust


def create_raw_table():
    cols = [
        ("Gold", "7,2"),
        ("CrudeOil", "6,3"),
        ("DowJones", "9,3"),
        ("SP500", "8,3"),
        ("NASDAQ", "8,3"),
        ("GlobalUSD", "8,3"),
        ("AsiaDJIA", "8,3"),
        ("NIKKEI225", "9,3"),
        ("FTSE100", "8,3"),
        ("EURUSD", "7,5"),
        ("USDJPY", "7,3"),
        ("USDCNY", "7,5"),
        ("US10YrNote", "6,4"),
        ("JP10YrBond", "6,4"),
        ("Ger10YrBond", "6,4")
    ]
    my_cursor.execute("CREATE TABLE raw_data (datetime DATETIME PRIMARY KEY NOT NULL)")
    data_type = "DECIMAL"
    for name, size in cols:
        my_cursor.execute(f"ALTER TABLE raw_data ADD COLUMN {name} {data_type}({size})")


def add_data(dt, col, val):
    my_cursor.execute()


def add_dt(dt, col, val):
    my_cursor.execute("")


def save_table(table_name):
    my_cursor.execute(f"show tables")
    my_cursor.fetchone()
    print(my_cursor)
    for dat in my_cursor:
        print(dat)


# create_raw_table()
# save_table("raw_data")
