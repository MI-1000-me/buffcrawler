from DrissionPage import Chromium
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
from DrissionPage.common import Settings
from DrissionPage.common import By

from cookie_manager import ensure_cookie



url= "https://buff.163.com/market/csgo#game=csgo" 
Settings.set_language('zh_cn')
bro= Chromium().latest_tab

def open_web(): 
    bro.set.cookies(manager.cookie)
    bro.get(url)
    return bro

        
def seek(name):
    ele= bro.ele('@placeholder=输入物品名称')
#    if not ele :
    ele.input(name)
    bro.ele('@id=search_btn_csgo').click()
    
        
def search():
    name= bro.ele("tag:li") 
    print(name.text)
    
# data-goods_id="857681" 
#title="AK-47（StatTrak™） | 墨岩 (略有磨损)"
# data-goods_id="911195" 
#title="印花 | Aleksib（闪耀）| 2022年里约热内卢锦标赛"
    """
    https://buff.163.com/market/csgo#game=csgo&page_num=2&search=ak-47
    """
    
if __name__ == "__main__":
    manager = ensure_cookie()
    open_web()
    seek("ak-47")
    search()
#https://buff.163.com/goods/857681饰品网址

# `url_available`
# 此属性以布尔值返回当前链接是否可用