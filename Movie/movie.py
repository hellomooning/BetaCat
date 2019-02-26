import tushare as ts
import Utils.utils as utils

def realtime_boxoffice():
    return ts.realtime_boxoffice()

def day_boxoffice(day=None):
    return ts.day_boxoffice(day)

if __name__ == '__main__':
    print(ts.day_boxoffice(utils.yesterday_date()))
