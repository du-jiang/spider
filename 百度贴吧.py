import requests
from lxml import etree

class tieba:
    def __init__(self,name):
        self.url = "https://tieba.baidu.com/f?kw={}&ie=utf-8&tab=good&cid=6".format(name)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
                        }
    def get_data(self,url): #发送请求获取响应
        res = requests.get(url,headers=self.headers)
        return res.content
    def parse_data(self,data):    #解析数据
        #创建element对象
        data = data.decode().replace("<!--", "").replace("-->", "")    # 源码中将数据注释
        html = etree.HTML(data)

        el_list =html.xpath('//div[@class="t_con cleafix"]/div[2]/div[1]/div[1]/a')
        data_list = []
        for el in el_list:
            temp = {}
            temp['title'] = el.xpath('./text()')[0]
            temp['link'] = 'http://tieba.baidu.com' + el.xpath('./@href')[0]
            data_list.append(temp)
        #以上提取了一页的标题和链接，下面开始翻页
        try:
            next_url = 'https:' + html.xpath('//a[contains(text(),"下一页")]/@href')[0]
        except:
            next_url = None
        return data_list, next_url
    def save_data(self,data_list):        #保存数据
        for data in data_list:
            print((data))

    def run(self):
        # url,headers
        # 发送请求获取响应
        next_url = self.url
        while True:
            data = self.get_data(next_url)
            # 提取数据和翻页用的url
            data_list, next_url = self.parse_data(data)
            self.save_data(data_list)
            #判断是否结束
            if next_url == None:
                break
if __name__ == '__main__':
    Tieba = tieba("单机游戏")
    Tieba.run()