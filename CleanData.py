import pandas as pd
import datetime

xlsx_file = r"Desktop\Data.xlsx"


def timestamp_to_datetime(time):
    return time.to_pydatetime().replace(second=0, microsecond=0)


def return_next_min(time):
    return time + datetime.timedelta(minutes=1)


def check_time(time1, time2):
    if time2 - time1 == datetime.timedelta(minutes=1):
        return True
    else:
        return False


df1 = pd.read_excel(xlsx_file)
df1["datetime"] = df1["datetime"].apply(lambda x: timestamp_to_datetime(x))
df1 = df1.set_index("datetime")
df2 = pd.DataFrame(df1.iloc[0:1])
df2 = pd.DataFrame(df1.iloc[0:1])
print(df1)


for i in range(1, len(df1.index)):
    time1 = pd.DataFrame(df1.iloc[i:i+1])
    time2 = pd.DataFrame(df2.iloc[-1])
    datetime1 = time1.index[0]
    datetime2 = time2.index[0]

    print(time1)
    print(time2)

    # datetime2 = time2["datetime"]
    print(datetime1)
    print(datetime2)

    # print(check_time(datetime1, datetime2))

    # time2 = pd.DataFrame(df2.iloc[-1])
    #
    # print(time1)
    # print(time2)
    break


# df2 = df2.append(df1.iloc[1:2])
# # df2 = df2.append(df1.iloc[1:2])
#
#
#
#
#
# print(df1)
# print(df2)


# f = open("testdata.csv", "a")
# f.write(df1.to_csv(index=False))
# f.close()
