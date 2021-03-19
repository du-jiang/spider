# coding=utf-8
import requests
import json
import sys

class Fanyi:
    def __init__(self, query_string):
        self.url1 = 'https://fanyi.baidu.com/langdetect'
        self.url2 = "https://fanyi.baidu.com/v2transapi"
        self.query_string = query_string
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Cookie': 'BIDUPSID=2D6DE836CB59FDA4D1D4C1930BB7641F; PSTM=1588605425; BAIDUID=2D6DE836CB59FDA432F2E5E0045883E0:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; delPer=0; PSINO=6; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=32292_1448_31670_32141_32360_31660_32352_32045_32393_32117_31640_22157; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1595163015,1595236467,1596020804; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1596020821; __yjsv5_shitong=1.0_7_95e4914734468c041a40322174c4ed720104_300_1596020820165_119.131.76.144_8a631b06; yjs_js_security_passport=927dd9563919c06bde851cb88b40002d497dd439_1596020863_js'
        }

    def get_post_data(self, ret):  # 1.url，post_data
        import execjs

        inputData = self.query_string

        with open("baidujs.js") as f:
            jsData = f.read()

        p = execjs.compile(jsData).call("e", inputData)

        post_data = {
            "query": self.query_string,
            "from": 'zh' if ret == 'zh' else 'en',
            "to": 'en' if ret == 'zh' else 'zh',
            "token": "6e11f1f93a76228dbccd6e367a5c09df",
            "sign": p
        }
        return post_data

    def parse_url(self, url2, data):  # 发送请求，获取响应
        resposne = requests.post(url2, data=data, headers=self.headers)
        return resposne.content.decode()

    def get_ret(self, json_str):  # 3.提取数据
        temp_dict = json.loads(json_str)
        # print(temp_dict)
        ret = temp_dict["trans_result"]['data'][0]["dst"]
        print("{} :{}".format(self.query_string, ret))

    def run(self):  # 实现主要逻辑
        data = {
            'query': self.query_string
        }
        resp = requests.post(self.url1, data=data, headers=self.headers)
        data_str = resp.content.decode()
        data_dict = json.loads(data_str)
        ret = data_dict['lan']
        # print(ret)

        # 1.url，post_data
        post_data = self.get_post_data(ret)
        # 2.发送请求，获取响应
        json_str = self.parse_url(self.url2, post_data)
        # print(json_str)
        # 3.提取数据
        self.get_ret(json_str)


if __name__ == '__main__':
    # query_string = sys.argv[1]
    while True:
        query_string = input('请输入内容(退出请输exit):')
        if query_string == 'exit':
            break
        fanyi = Fanyi(query_string)
        fanyi.run()