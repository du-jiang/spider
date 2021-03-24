import requests
import json
from Crypto.Cipher import AES
from base64 import b64encode
data = {
        "csrf_token": "",
        "cursor": "-1",
        "offset": "0",
        "orderType": "1",
        "pageNo": "1",
        "pageSize": "20",
        "rid": "R_SO_4_1830079389",
        "threadId": "R_SO_4_1830079389"
    }
i = "YjBUvSm1FlkzmleT"
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
class music(object):
    def __init__(self):
        self.url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        }


    def get_data(self):
        res = requests.post(url=self.url, headers=self.headers, data={
            "params": self.get_params(json.dumps(data)),
            "encSecKey": self.get_encSecKey()
        })
        x = json.loads(res.text)
        #         # print(x)
        for y in x["data"]["comments"]:
            print(y["content"])
        for z in x["data"]["hotComments"]:
            print(z["content"])

        return res

    def run(self):
        #url,headers
        self.get_data()

        #发送请求获取响应
        #解析响应
        #进入歌曲链接爬取评论


    """
    解密过程
        函数a：完全随机字符串
        function a(a) {
            var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
            for (d = 0; a > d; d += 1) 下面d中的a(16)，所以是循环16次
                e = Math.random() * b.length,随机数
                e = Math.floor(e),取整
                c += b.charAt(e);取上边的字符串中的e位置
            return c
        }
        函数b：
        function b(a, b) {   a是要加密的内容   b是密钥
            var c = CryptoJS.enc.Utf8.parse(b)  c=经过编码的密钥
              , d = CryptoJS.enc.Utf8.parse("0102030405060708")  d=经过编码的"0102030405060708"
              , e = CryptoJS.enc.Utf8.parse(a)  e=经过编码的要加密的内容
              , f = CryptoJS.AES.encrypt(e, c, {      AES加密
                iv: d, 偏移量
                mode: CryptoJS.mode.CBC 加密模型
            });
            return f.toString()
        }
        function c(a, b, c) {
            var d, e;
            return setMaxDigits(131),
            d = new RSAKeyPair(b,"",c),
            e = encryptedString(d, a)
        }
        function d(d, e, f, g) {            d：数据data   e：将bsK6E(["流泪", "强"])放入console得出固定值"010001"
            var h = {}                      f:同e得出"00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
              , i = a(16);随机16位字符串      g:"0CoJUm6Qyw8W8jud"
            return h.encText = b(d, g),         h.encText = b(d, g)         可以看到encText是双重AES加密，
            h.encText = b(h.encText, i),------》h.encText = b(h.encText, i)  写在下面
            h.encSecKey = c(i, e, f),           h.encSecKey = c(i, e, f)    encSecKey写在下面
            h                                   return h
        }
    ---------------------------------------
    var bWv4z = window.asrsea(JSON.stringify(i3x), bsK6E(["流泪", "强"]), bsK6E(XR0x.md), bsK6E(["爱心", "女孩", "惊恐", "大笑"]));
    因为上面这行是加密，下面又window.asrsea = d 赋值给了d，所以先看函数d，四个参数对应上面四个参数

    注意：AES加密要求加密内容的长度必须是16的倍数，少的位数需要用缺少的位数个chr(缺少的位数)补齐，如果是16个则需补16个chr(16)
    encText的双重加密
    第一次加密：将数据和g作为参数传给函数b   h.encText = b(d, g) 根据函数b  d是数据g是密钥
    第二次加密：将第一次加密的结果作为数据和随机数i作为参数传给函数b，然后得到params
    encSecKey：可以看到h.encSecKey = c(i, e, f)，函数c的这三个参数只有i是不固定的，上面的函数c中也没有随机，因此可以
    将i固定，这样无论函数c中的RSA加密怎样变动，encSecKey都是不变的
    """

    def get_encSecKey(self):
        return "5f34a5babb62fd922a51a2abfe42a92bb4010eb374a8020340194257adadc52b921db1722f623dcd566af43a369633bf055b02e7dfb7144af54014572209681af2851e085ab61405b4b36cc02f146ae8334b0becc471aee6cfa18da53fdea848f8416bb6ccf1b4fc0b2076d9d506c813d9ec96651b9a8d3d7c90a60870683005"

    def get_params(self, data):
        first = self.jiami(data, g)
        second = self.jiami(first, i)
        return second
    def AES_rules(self, data):
        a = 16 - len(data) % 16
        data += chr(a) * a
        return data
    def jiami(self, data, key):   #还原AES加密
        IV = "0102030405060708"
        data = self.AES_rules(data)
        aes = AES.new(key=key.encode("utf-8"), IV=IV.encode("utf-8"), mode=AES.MODE_CBC)
        bs = aes.encrypt(data.encode("utf-8"))#加密
        return str(b64encode(bs), "utf-8")
if __name__ == '__main__':
    Music = music()
    Music.run()