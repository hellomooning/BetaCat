import tushare as ts

def top_list(date):
    return ts.top_list(date)

def cap_tops(days=5):
    return ts.cap_tops(days)

def broker_tops(days=5):
    return ts.broker_tops(days)

def inst_detail():
    return ts.inst_detail()

def inst_tops():
    return ts.inst_tops()

if __name__ == '__main__':
    print(inst_tops())
