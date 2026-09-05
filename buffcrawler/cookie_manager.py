import json
import logging
from pathlib import Path

from DrissionPage import ChromiumOptions
from DrissionPage import Chromium

from config import buff_url,log_config
logging_config= log_config

co = ChromiumOptions()
co.headless(False) # 非无头模式


class BuffCookieManager():
    def __init__(self):
        self.bro= Chromium(addr_or_opts=co).latest_tab
        self.url= buff_url
        self.cookie = None
        
    def get_cookie(self) -> list:
        """ 
        扫码登入，读取cookie，然后返回cookie
        """
        self.bro.get(self.url)
        input("扫码后按回车")
        self.cookie= self.bro.cookies()
        if not self.cookie: 
            logging.warning("cookie未成功读取") 
            self.bro.wait.ele_displayed('@text()=我的库存') 
            self.cookie= self.bro.cookies() 
        return self.cookie

    def store_cookie(self):
        #写入cookie到json以便多次存储cookie
        with open("cookie.json","w",encoding="utf8")as cooi:
            logging.info("正在写入cookie")
            json.dump(self.cookie, cooi)
            
    def test_cookie(self):
        """
        通过检验是否有"我的库存"元素，来检验是否登入账号。以及检验账号是否被封
        """
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

    def open_cookie(self):
        """
        读取cookie从json，然后加载此cookie
        """
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
        self.bro.browser.quit()

def has_cookie():
    """检查当前目录是否存在 cookie.json"""
    cookie_file = Path("cookie.json")
    return cookie_file.exists()

def ensure_cookie()->BuffCookieManager:
    """
        确保程序拥有一个可用的 Buff Cookie。

        流程：
        1. 检查本地是否存在 cookie.json
        2. 不存在则打开浏览器登录并保存 Cookie
        3. 存在则读取本地 Cookie
        4. 校验 Cookie 是否仍然有效
        5. Cookie 失效则重新登录并更新 Cookie

        返回：
            BuffCookieManager 对象，
            可通过 .cookie 获取当前 Cookie 数据。
    """
    
    cookie = BuffCookieManager()

    # 首次运行，没有本地 Cookie 文件
    if not has_cookie():
        cookie.get_cookie()
        cookie.store_cookie()

    else:
        # 读取本地 Cookie
        cookie.open_cookie()

        # Cookie 失效则重新登录
        if not cookie.test_cookie():
            cookie.get_cookie()
            cookie.store_cookie()
            logging.critical("cookie校验失败")

    # 最终检查是否成功获取到 Cookie
    if not cookie.cookie:
        logging.error("cookie未成功读取")

    return cookie
        

if __name__ == "__main__":
    ensure_cookie()