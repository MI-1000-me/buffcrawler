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
manager = ensure_cookie()

def open_web(): 
    bro.set.cookies(manager.cookie)
    bro.get(url)
    return bro

        
def search():
    names= bro.eles(".cols")
    for link in names:
        # 打印链接信息
        print(link.text, link.link)
        #注意一个种类结束link.link是none
    return names
    

if __name__ == "__main__":

    open_web()
    search()

