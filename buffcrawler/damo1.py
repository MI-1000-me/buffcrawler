from DrissionPage import Chromium
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
from DrissionPage.common import Settings
from DrissionPage.common import By

from get_cookie import getCookie

url= "https://buff.163.com/market/csgo#game=csgo" 
Settings.set_language('zh_cn')
bro= Chromium().latest_tab

def open_web(): 
    
    bro.get(url)
    return bro


def ensure_login():
    
    open_web()
    bro.ele('@id=search_btn_csgo').click()
    if bro.ele('@text()=扫描上方二维码登录'):
        user_cookie= getCookie(url)
        bro.set.cookies(user_cookie)
        bro.get(url)
        
        
def seek(name):
    
    ele= bro.ele('@placeholder=输入物品名称')
    ele.input(name)
    bro.ele('@id=search_btn_csgo').click()


    
if __name__ == "__main__":
    ensure_login()
    seek("ak")
# `url_available`
# 此属性以布尔值返回当前链接是否可用