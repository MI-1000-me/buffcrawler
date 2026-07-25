import json
from pathlib import Path

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
        input("扫码后按回车")
        self.cookie= self.bro.cookies()
        return self.cookie

    #储存cookie
    def store_cookie(self):
        with open("cookie.json","w",encoding="utf8")as cooi:
            json.dump(self.cookie, cooi)
            
    #校验cookie
    def test_cookie(self):
        if self.cookie:
            self.bro.set.cookies(self.cookie)
        self.bro.get(self.url)  
        if self.bro.ele('@text()=我的库存') is None:
            return False
        return True
    
    #打开cookie
    def open_cookie(self):
        with open("cookie.json","r",encoding="utf8")as cooi:
            self.cookie = json.load(cooi)
        return self.cookie

def has_cookie():
    """检查当前目录是否存在 cookie.json"""
    cookie_file = Path("cookie.json")
    return cookie_file.exists()

def ensure_cookie():
    #控制函数
    
    cookie= CookieManager()
    
    if not  has_cookie() :
        cookie.get_cookie()
        cookie.store_cookie()
    else:
        cookie.open_cookie()
        
        if not cookie.test_cookie():
            cookie.get_cookie()
            cookie.store_cookie()
    return cookie
        

if __name__ == "__main__":
    ensure_cookie()