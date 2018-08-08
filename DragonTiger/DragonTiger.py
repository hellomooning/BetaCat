import tushare as ts
import Utils.utils as utils

def get_top_list(date):
    return ts.top_list(date)

def get_cap_tops(days=30):
    return ts.cap_tops(days)

if __name__ == '__main__':
    print(get_cap_tops())
