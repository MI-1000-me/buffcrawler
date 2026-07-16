import json

from DrissionPage import Chromium

url="https://buff.163.com/market/csgo#game=csgo"

class CookieManager():
    def __init__(self):
        self.bro= Chromium().latest_tab
        self.url= url
        self.cookie = None
        
    #获取cookie
    def get_cookie(self):
        self.bro.get(self.url)
        self.cookie= self.bro.cookies()
        return self.cookie

    #储存cookie
    def store_cookie(self):
        with open("cookie.json","w",encoding="utf8")as cooi:
            json.dump(self.cookie, cooi)
    #校验cookie
    def test_cookie(self):
        self.bro.ele('@id=search_btn_csgo').click()
        if self.bro.ele('@text()=扫描上方二维码登录'):
            if self.cookie:
                self.bro.set.cookies(self.cookie)
            self.bro.get(self.url)
    #打开cookie
    def open_cookie(self):
        with open("cookie.json","r",encoding="utf8")as cooi:
            cookie = json.load(cooi)
        return self.cookie


def ensure_cookie():
    #控制函数
    pass

""" 
创建 CookieManager
        │
        ▼
    读取 Cookie
        │
        ▼
    验证 Cookie
        │
   ┌────┴────┐
   │         │
有效       无效
   │         │
直接返回   扫码登录
             │
             ▼
         获取 Cookie
             │
             ▼
          保存 Cookie
             │
             ▼
           返回 Cookie
"""