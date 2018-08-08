import datetime as dt

def datetime():
    return dt.datetime.now()

def date():
    return str(dt.date.today())

def yesterday_date():
    return str(dt.date.today() - dt.timedelta(days=1))

if __name__ == '__main__':
    print(yesterday_date())
