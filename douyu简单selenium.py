from selenium import webdriver

import time
class douyu(object):
    def __init__(self):
        self.url = "https://www.douyu.com/g_LOL"
        self.driver = webdriver.Chrome()
    def parse_data(self):
        room_list = self.driver.find_elements_by_xpath('//li[@class="layout-Cover-item"]/div')
        #获取节点数据
        for room in room_list:
            try:
                temp = {}
                temp['title'] = room.find_element_by_xpath('./a/div[2]/div[1]/h3').text
                temp['type'] = room.find_element_by_xpath('./a/div[2]/div[1]/span').text
                temp['boss'] = room.find_element_by_xpath('./a/div[2]/div[2]/h2/div').text
                temp['num'] = room.find_element_by_xpath('./a/div[2]/div[2]/span').text
                print(temp)
            except:
                pass


    def run(self):
        #url
        #dirver
        #get
        self.driver.get(self.url)
        #parse
        self.parse_data()
        #save
        #next
if __name__ == '__main__':
    Douyu = douyu()
    Douyu.run()