from DrissionPage import Chromium
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
from DrissionPage.common import Settings
from DrissionPage.common import By

from get_cookie import getCookie
#明天把控制函数写完这里要改

url= "https://buff.163.com/market/csgo#game=csgo" 
Settings.set_language('zh_cn')
bro= Chromium().latest_tab

def open_web(): 
    
    bro.get(url)
    return bro

        
def seek(name):
    #这里ele有问题，改。还有最下面的id重了要找新的
    input1= ["输入物品名称","Enter the item name"]
    ele= bro.ele(f'@placeholder={input1}')
    ele.input(name)
    bro.ele('@id=search_btn_csgo').click()
        
"""
校验cookies在现在的getcookie写完了，到时候改完重新写openweb流程
"""

    
if __name__ == "__main__":
    seek("ak")
# `url_available`
# 此属性以布尔值返回当前链接是否可用