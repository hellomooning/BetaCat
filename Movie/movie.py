import tushare as ts
import Utils.utils as utils

def realtime_boxoffice():
    return ts.realtime_boxoffice()

def day_boxoffice(day=None):
    return ts.day_boxoffice(day)

def test():
    ts.set_token('711951da99614027f5fbbfcfd64a2af751e903a519d12ebdb58422ef')
    pro = ts.pro_api()
    return pro.moneyflow(trade_date='20190315')

if __name__ == '__main__':
    print(ts.day_boxoffice(utils.yesterday_date()))
