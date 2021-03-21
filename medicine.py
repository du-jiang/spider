import requests
import pandas as pd
import pandas
from openpyxl import load_workbook
import xlwt
#
url = 'http://code.nhsa.gov.cn:8000/yp/getPublishGoodsDataInfo.html'
headers = {
    'Host': 'code.nhsa.gov.cn:8000',
    'Referer': 'http://code.nhsa.gov.cn:8000/yp/toPublishGoodsData.html?batchNumber=20191205',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}
k = 1

for i in range(1,4):
    params = {
        'batchNumber': '20191205',
        '_search': 'false',
        'nd': '1576048139781',
        'rows': '50',
        'page': i,
        'sidx': 't.goods_code',
        'sord': 'asc'
    }
    response = requests.post(url,headers=headers,params=params)
    a = response.json()
#     print(a)
    b = {"rows"}
    # 字典的形式
    c = { key:value for key,value in a.items() if key in b }
#     print(c)
    d = list(c.values())
#     print(d)
    
    e = []
    g = []
    b = []
    for _ in d:
        e += _
#         print(e)
        for f in e:
#             print(f)
            f1 = f['approvalcode']
#             print(f1)
            g.append(f1)
            c = (pd.DataFrame(g))
            book = load_workbook('C://Users//Administrator//Desktop//666.xlsx')
            writer = pandas.ExcelWriter('C://Users//Administrator//Desktop//666.xlsx', engine='openpyxl') 
            writer.book = book
            writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
              
    c.to_excel(writer,sheet_name='sheet'+str(i))
    writer.save()
    
            
        