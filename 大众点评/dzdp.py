from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
import numpy
from pytesseract import pytesseract
import requests
import re
import time
from lxml import etree
import json
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
#         'Cookie': '_lxsdk_cuid=17887405becc8-09483430d421ca-5771031-100200-17887405becc8; _lxsdk=17887405becc8-09483430d421ca-5771031-100200-17887405becc8; _hc.v=e8ac1d54-b772-9a81-0452-9cf41f388bf5.1617176845; s_ViewType=10; ctu=614fe8413f58001ebb7e771980f3aa4f5a8513f95756f1aab8a8316ccd7f2232; ua=%E4%B8%8D%E8%A6%81%E7%83%A7%E6%88%91%E7%9A%84%E8%8A%B1%E6%9E%9C%E5%B1%B1; cy=50; cye=tongliao; fspop=test; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1618465852,1618545421,1618819392,1619398019; dplet=2b5827d793db69bea63714bb1b13f910; dper=3feff70dbfd6af50e5c4ee2a0ab929668f14154f44e5260c3258055e295bc95371e0a671e41d47825557f1b76cd71237fb9cef5b1d2098ea406657d2cafc98adb7401d4c07a683b832075ab3a81b40567c36eeed0c4f063d8b33f8e8bb2a1cef; ll=7fd06e815b796be3df069dec7836c3df; aburl=1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=1790ccb389a-8db-30b-947%7C%7C41; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1619417324',
#         'Host': 'www.dianping.com',
#         'Accept': 'text/html,application/xht
#         ml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
# }
# for i in range(50):
#     url = 'http://www.dianping.com/tongliao/ch10/p{}'.format(i)
#     response = requests.get(url=url, headers=headers)
#     with open('./大众点评/第{}页.html'.format(i), 'w', encoding='utf-8')as f:
#         f.write(response.text)
#         time.sleep(30)
# font1 = TTFont('31c7b648.woff')    # 打开文件
font1 = TTFont('1477d475.woff')    # 打开文件
font2 = TTFont('e3e9e89b.woff')    # 打开文件
# font2 = TTFont('238d0d9e.woff')    # 打开文件
font3 = TTFont('1477d475.woff')    # 打开文件
# font3 = TTFont('12359f07.woff')    # 打开文件
font4 = TTFont('e3e9e89b.woff')    # 打开文件
# font4 = TTFont('baf747e5.woff')    # 打开文件
fonts = [font1, font2, font3, font4]
font_path = ['e3e9e89b.woff', '238d0d9e.woff', '12359f07.woff', 'baf747e5.woff']
# font1.saveXML('address.xml')     # 转换成 xml 文件并保存
# font2.saveXML('tagName.xml')     # 转换成 xml 文件并保存
# font3.saveXML('shopNum.xml')     # 转换成 xml 文件并保存
# font4.saveXML('reviewTag.xml')     # 转换成 xml 文件并保存
a = 0
for font in fonts:
    codeList = font.getGlyphOrder()[2:]
    im = Image.new("RGB", (1800, 1000), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_path[a], 40)
    a += 1
    count = 15
    arrayList = numpy.array_split(codeList,count)   #将列表切分成15份，以便于在图片上分行显示
    for t in range(count):
        newList = [i.replace("uni", "\\u") for i in arrayList[t]]
        text = "".join(newList)
        text = text.encode('utf-8').decode('unicode_escape')
        dr.text((0, 50 * t), text, font=font, fill="#000000")
    im.save("img.jpg")
    im = Image.open("sss.jpg")      #可以将图片保存到本地，以便于手动打开图片查看
    result = pytesseract.image_to_string(im, lang="chi_sim")
    result = result.replace(" ","").replace("\n","")
    codeList = [i.replace("uni","&#x")+";" for i in codeList]
    svg = dict(zip(codeList, list(result)))
    print(svg)
    # 替换
#
#     for x in range(50):
#         if a == 0:
#             with open('./大众点评/第{}页.html'.format(x), 'r', encoding='utf-8')as f:
#                 res = f.read()
#             a1 = re.findall(r'<svgmtsi class="address">(.*?);</svgmtsi>', res)
#             for b in a1:
#                 for k, v in svg.items():
#                     if b == str(list(k)[0]):
#                         r = res.replace(b, list(v)[0])
#
#         if a == 1:
#             with open('./大众点评/第{}页.html'.format(x), 'r', encoding='utf-8')as f:
#                 res = f.read()
#             a2 = re.findall(r'<svgmtsi class="tagName">(.*?);</svgmtsi>', res)
#             for b in a2:
#                 for k, v in svg.items():
#                     if b == str(list(k)[0]):
#                         r = res.replace(b, list(v)[0])
#
#         if a == 2:
#             with open('./大众点评/第{}页.html'.format(x), 'r', encoding='utf-8')as f:
#                 res = f.read()
#             a3 = re.findall(r'<svgmtsi class="shopNum">(.*?);</svgmtsi>', res)
#             for b in a3:
#                 for k, v in svg.items():
#                     if b == str(list(k)[0]):
#                         r = res.replace(b, list(v)[0])
#
#         if a == 3:
#             with open('./大众点评/第{}页.html'.format(x), 'r', encoding='utf-8')as f:
#                 res = f.read()
#             a4 = re.findall(r'<svgmtsi class="reviewTag">(.*?);</svgmtsi>', res)
#             for b in a4:
#                 for k, v in svg.items():
#                     if b == str(list(k)[0]):
#                         r = res.replace(b, list(v)[0])
# shop_message = []
# shop_list = []
# # score_list = []
# # comment_list = []
# # price_list = []
# # dish_sort_list = []
# # address_list = []
# # recommend_list = []
# # Taste_list = []
# # setting_list = []
# # service_list = []
# for i in range(50):
#     with open('./大众点评/第{}页.html'.format(i), 'r', encoding='utf-8')as f:
#         res = f.read()
#     html = etree.HTML(res)
#     for u in range(1, 16):
#         shop = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/div[1]/a/h4/text()'.format(u))
#         score = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/div[2]/div/div[2]/text()'.format(u))
#         comment_num1 = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/div[2]/a[1]/b/text()'.format(u))
#         comment_num2 = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/div[2]/a[1]/text()'.format(u))
#         comment_num = comment_num1[0] + comment_num2[0]
#         price1 = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/div[2]/a[2]/text()'.format(u))
#         price2 = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/div[2]/a[2]/b/text()'.format(u))
#         price = price1[0] + price2[0]
#         dish_sort = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/div[3]/a[1]/span/text()'.format(u))
#         address1 = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/div[3]/a[2]/span/text()'.format(u))
#         address2 = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/div[3]/span/text()'.format(u))
#         address = address1[0] + address2[0]
#         try:
#             recommend1 = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/div[4]/span/text()'.format(u))
#             recommend2 = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/div[4]/a/text()'.format(u))
#             if recommend1 == [] or recommend2 == []:
#                 recommend = ["无"]
#             else:
#                 recommend = []
#                 recommend.append(recommend1, recommend2)
#         except:
#             recommend = ["无"]
#         Taste1 = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/span/span[1]/text()'.format(u))
#         Taste2 = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/span/span[1]/b/text()'.format(u))
#         Taste = Taste1[0] + Taste2[0]
#         setting1 = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/span/span[2]/text()'.format(u))
#         setting2 = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/span/span[2]/b/text()'.format(u))
#         settings = setting1[0] + setting2[0]
#         service1 = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/span/span[3]/text()'.format(u))
#         service2 = html.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/span/span[3]/b/text()'.format(u))
#         service = service1[0] + service2[0]
#
#         print(shop)
#         shop_message.append(str(shop[0], score[0], comment_num[0], price[0], dish_sort[0], address[0], recommend[0], Taste[0], settings[0], service[0]))
#         shop_list.append(shop[0])
#         # score_list.append(score)
#         # comment_list.append(comment_num)
#         # price_list.append(price)
#         # dish_sort_list.append(dish_sort)
#         # address_list.append(address)
#         # recommend_list.append(recommend)
#         # Taste_list.append(Taste)
#         # setting_list.append(settings)
#         # service_list.append(service)
#
# print(shop_list)
# with open('大众点评.txt', 'w', encoding='utf-8')as f:
#     for g in shop_message:
#         f.write(g + '\n')
