from DrissionPage import Chromium
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
from DrissionPage.common import Settings
from DrissionPage.common import By

from cookie_manager import ensure_cookie

co = ChromiumOptions()
co.headless(True)  # 无头模式
co.no_imgs(True)   # 禁用图片
  
url= "https://buff.163.com/market/csgo#game=csgo" 
Settings.set_language('zh_cn')
bro= Chromium(addr_or_opts=co).latest_tab

def open_web(): 
    bro.set.cookies(manager.cookie)
    bro.get(url)
    return bro

        
def search():
    name= bro.ele(".cols").text
    return name

if __name__ == "__main__":
    manager = ensure_cookie()
    open_web()
    search()
