import json
import logging
from pathlib import Path

from DrissionPage import ChromiumOptions
from DrissionPage import Chromium

url="https://buff.163.com/market/csgo#game=csgo"

logging.basicConfig(
                    level=logging.INFO,
                    format="%(levelname)s - %(asctime)s - %(funcName)s - %(message)s",
                     datefmt="%Y-%m-%d %H:%M:%S",
                     filename="cookies.log",
                     filemode="a",
                     encoding= "utf-8",
                     )

co = ChromiumOptions()
co.headless(False) # 非无头模式

class BuffCookieManager():
    def __init__(self):
        self.bro= Chromium(addr_or_opts=co).latest_tab
        self.url= url
        self.cookie = None
        
    #获取cookie
    def get_cookie(self) -> list:
        self.bro.get(self.url)
        input("扫码后按回车")
        self.cookie= self.bro.cookies()
        if not self.cookie:
            logging.error("cookie未成功读取")
        return self.cookie

    #储存cookie
    def store_cookie(self):
        with open("cookie.json","w",encoding="utf8")as cooi:
            logging.info("正在写入cookie")
            json.dump(self.cookie, cooi)
            
    #校验cookie
    def test_cookie(self):
        if self.cookie:
            self.bro.set.cookies(self.cookie)
        self.bro.get(self.url)  
        if self.bro.ele('@text()=我的库存') is None:
            print("暂未登录")
            return False
        else:
            if self.bro.ele('@text()=市场接口访问功能暂时关闭') is None:
                self.cookie= self.bro.cookies()
                return True
            else:
                print("cookie已过期")
                self.bro.set.cookies.clear() 
                self.bro.refresh()
                print("请重新扫码登录")
                return False

    #打开cookie
    def open_cookie(self):
        try:
            with open("cookie.json","r",encoding="utf8") as f:
                self.cookie = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.cookie = None

    #关闭浏览器
    def close(self):
        logging.info("已关闭浏览器")
        self.browser = Chromium(addr_or_opts=co)
        self.bro = self.browser.latest_tab

def has_cookie():
    """检查当前目录是否存在 cookie.json"""
    cookie_file = Path("cookie.json")
    return cookie_file.exists()

def ensure_cookie()->BuffCookieManager:
    #控制函数
    
    cookie= BuffCookieManager()
    
    if not  has_cookie() :
        cookie.get_cookie()
        cookie.store_cookie()
    else:
        cookie.open_cookie()
        
        if cookie.test_cookie() == False:
            cookie.get_cookie()
            cookie.store_cookie()
            logging.critical("cookie校验失败")
    if not cookie.cookie: 
        logging.error("cookie未成功读取")
    return cookie
        

if __name__ == "__main__":
    ensure_cookie()