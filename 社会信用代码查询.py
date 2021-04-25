from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from io import BytesIO
from PIL import Image
from selenium.webdriver import ActionChains
import cv2
import sys

class MeiZu(object):
    def __init__(self):
        self.url = "https://www.cods.org.cn/"
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.account = '123456789'

    def input_account(self):
        #输入查询内容
        self.browser.get(self.url)
        sleep(1)
        self.wait.until(ec.presence_of_element_located((By.ID, 'checkContent_index'))).send_keys(self.account)
        sleep(0.6)

    def get_button(self):
        # 点击搜索
        button = self.wait.until(ec.element_to_be_clickable((By.ID, 'checkBtn')))
        return button

    def get_position(self):
        # 获取验证码像素位置
        img = self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        sleep(2)
        location = img.location
        size = img.size
        left, top, right, button = location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']
        return left, top, right, button

    def get_screenshot(self):
        # 获取网页截图
        self.browser.get_screenshot_as_file('html.png')
        # 将验证码图片从网页截图中抠出
        left, top, right, button = self.get_position()
        img = Image.open('html.png')
        imge = img.crop((left, top, right, button))
        imge.save('yzm.png')

    def get_slider(self):
        # 获取滑块按钮
        slider = self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    def get_len(self):
        #计算位移
        im = Image.open('yzm.png')
        get_len = 0
        for x in range(im.size[0]):
            a = 0
            for y in range(im.size[1]):
                rgb = im.load()[x, y]
                if rgb[0] < 20 and rgb[1] < 60 and rgb[2] < 90:
                    a += 1
                if a > 10:
                    return x
        return get_len

    def reback(self):
        #计算错误重试
        # distence = self.get_len()
        # if distence == 0 or distence >= 160:
        #计算错误点击刷新
        self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'geetest_refresh_1')))
        self.browser.find_element_by_class_name('geetest_refresh_1').click()

    def huadong(self):
        #滑动滑块,模仿人类行为轨迹，避免图片被怪兽吃掉
        action_chains = webdriver.ActionChains(self.browser)
        action_chains.click_and_hold(self.get_slider())
        action_chains.pause(0.2)
        action_chains.move_by_offset(self.get_len() - 5, 0)
        action_chains.pause(0.6)
        action_chains.move_by_offset(-5, 0)
        action_chains.pause(0.6)
        action_chains.move_by_offset(+5, 0)
        action_chains.pause(0.8)
        action_chains.move_by_offset(-5, 0)
        action_chains.pause(0.9)
        action_chains.release()
        action_chains.perform()
        sleep(4)

    def run(self):
        # 输入查询内容
        self.input_account()
        # 点击搜索
        button = self.get_button()
        # button.click()会出现兼容问题报错，所以用js来执行点击
        self.browser.execute_script('arguments[0].click();', button)
        sleep(3)
        self.browser.refresh()

        while True:
            for i in range(4):
                if i == 3:
                    print("未成功，刷新")
                    self.browser.refresh()
                else:
                    # 获取验证码图片
                    self.get_screenshot()
                    # 计算缺口位置/滑动长度
                    distence = self.get_len()
                    # 如果滑动长度计算错误则刷新
                    if distence == 0 or distence >= 160:
                        self.reback()
                        continue
                    else:
                        # 拖动滑块
                        self.huadong()
                    if self.browser.title == 'sorry':
                        self.browser.quit()
                        sys.exit()




if __name__ == '__main__':
    meizu = MeiZu()
    meizu.run()












