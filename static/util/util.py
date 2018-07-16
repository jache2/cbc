import requests
import pandas

trade_type_expenditure = 1;
trade_type_income = 2;
def getBalance(address):
    getBalanceUrl = 'https://block.chainedbox.com/index/GetBalance'
    res = requests.post(getBalanceUrl,{'address':address})
    return res.json().get('res').get('accounts')[0].get('balance')

def getPageContent(address, tradeType, start):
    eventScan = 'https://block.chainedbox.com/index/EventScan'
    res3 = requests.post(eventScan,{'address':address,'type':tradeType,'start':start})
    return res3.json()

def getContent(res):
    return res.get('res').get('events').get('list')

def getPageStart(res):
    return res.get('res').get('events').get('start')

def getList(address):
    ret = []
    next = ''
    while(1>0):
        content = getPageContent(address,trade_type_expenditure,next)
        next = getPageStart(content)
        print(next)
        if(next != ''):
            list = getContent(content)
            ret.extend(list)
        else:
            return ret

def install():
    # ddd
if __name__ == '__main__':
    address = '0x0052D554f6B47286d02739942242037ca5A6202B'
    print("可用余额："+getBalance(address))
    list = getList(address)
    print(list.__len__())
    df = pandas.DataFrame(list)
    df.to_csv("//Users/zhucheng/aa.csv")



