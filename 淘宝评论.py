#encoding:utf-8
import json
import requests
import csv

headers = {
    "cookie": "dnk=%5Cu674E%5Cu897F%5Cu74DC3; t=e084d0ff3438e55e02b4bd0f3940a782; lid=%E6%9D%8E%E8%A5%BF%E7%93%9C3; _tb_token_=8fe596b9e0b5; cookie2=1ed157aa4da72014b0401c2c468425e7; enc=cLGI69iGuHhR5dHEyCu674E%5Cu897F%5Cu74DC3; uc4=nk4=0%40oaXu7yh9pdCZTaRJY7qDotYR&id4=0%40U2uE9bgavzU7dxkYCPk4vP%2F1op69; lgc=%5Cu674E%5Cu897F%5Cu74DC3; sgcookie=EIrgPgb1qADYh9IUfx2JY; csg=883d7d47; _m_h5_tk=fef5251ec2478fcdbbaeaa83cea3acf9_1587199947953; _m_h5_tk_enc=1f5dbcd059904d7035151f823874efe2; tfstk=c9DRBv_NpEYuLJiz_vd0deSXjokRZ8j8-gadpH6GIES9fvXdirHiB5iBNk78HnC..; x5sec=7b22726174656d616e616765723b32223a223062623832303465303837663365616536616530326538623862653636323834435057332f2f5146454e57796b3447497875716b7341453d227d; OZ_SI_2061=sTime=1587532108&sIndex=25; OZ_1U_2061=vid=ve9fd14cbef42e.0&ctime=1587535343&ltime=1587535336; OZ_1Y_2061=erefer=https%3A//kb-render.alicdn.com/html/61574/2020/04/17/5a47a178-0d8d80e8-120425885.html%3Frd%3Dhttps%253A%252F%252Fclick.mz.simba.taobao.com%252Fbrand%253Fe%253D6B%25252FcjhXDKa6jVNTaFT64%25252Bb9DF67xy%252526NfUUPlE8tgezaquuKfLDrni1SKmG9%25252FSppqtsZTksZxmREkdsuPsCamr8WVqNcfHdhVdOCq6IIdOCZMxKbtd687c86rR9eOOepHFbKvafqb0Q3zD0BqzDf03%25252B%252593%587535343&ltime=1587535336&compid=2061; isg=BMbGq4Yu5E7RK7Mw6jD4gEaoF7xIhIRVguPzaNbMiT5P9w595moAWZX3gyTpCnGVn6lHR3JMwUX8B58UmPathZXRFJXn9MptndLh.",
    "referer": "https://detail.tmall.com/item.htm",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
}
ids = "633908800326"
title = ids



params = {
    "itemId": ids,
    "sellerId": "196993935",
    "currentPage": "1",
    "callback": "jsonp723"
}

def request_comment(page):

    url = "https://rate.tmall.com/list_detail_rate.htm"
    params["currentPage"] = str(page)
    req = requests.get(url, params, headers=headers).content.decode('utf-8')[11:-1]
    return req


def comment_crawl(itemId, pages, writer):
    params["itemId"] = str(itemId)
    # 爬取的表格属性
    attris = ["displayUserNick", "auctionSku", "rateDate", "rateContent"]
    csv_writer = csv.writer(writer)
    csv_writer.writerow(attris)
    # 读取pages页评论
    for i in range(pages):
        page = i + 1
        print('当前正在下载第%d页评论' % (page))
        req = request_comment(page)
        result = json.loads(req)
        comments = result["rateDetail"]["rateList"]
        for comment in comments:
            tmp = []
            for attri in attris:
                tmp.append(comment[attri])
            csv_writer.writerow(tmp)


writer = open(f"{title}.csv", "w", newline='', encoding='utf-8-sig')
itemId = ids
comment_crawl(itemId, 10, writer)
writer.close()
