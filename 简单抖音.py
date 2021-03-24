import requests

class douyin(object):
    def __init__(self):
        self.url = "https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAyZDEIZXVhG70PyvBB0NMUIMMTOEP3R48Hz1xLEs-Ebo&count=50&max_cursor=0&aid=1128&_signature=Hr7M2AAAfuv2ZO6lbXsBJh6-zM&dytk="
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36x-requested-with: XMLHttpRequest"
        }
    def get_link(self):
        res = requests.get(url=self.url, headers=self.headers).json()
        aweme_list = res["aweme_list"]
        for i in aweme_list:
            video = i["video"]["play_addr"]["url_list"][0]
            name = i["desc"]
            self.get_video(url=video, name=name)
    def get_video(self,url,name):
        response = requests.get(url=url, headers=self.headers)
        with open("F:/猫猫/{}.mp4".format(name), "ab")as f:
            f.write(response.content)

if __name__ == '__main__':
    Douyin = douyin()
    Douyin.get_link()
