import logging

from DrissionPage import Chromium
from DrissionPage import ChromiumOptions
from DrissionPage.common import Settings
from pathlib import Path


from cookie_manager import ensure_cookie
from config import buff_url,log_config
logging_config= log_config

co = ChromiumOptions()
co.headless(True)  # 无头模式
co.no_imgs(True)   # 禁用图片
co.incognito()     # 无痕模式



manager = ensure_cookie()  
url= buff_url
Settings.set_language('zh_cn')
bro= Chromium(addr_or_opts=co).latest_tab


def open_web(): 
    bro.set.user_agent( 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36')
    bro.set.cookies(manager.cookie)
    bro.get(url)
    return bro

        
def search(bro)->tuple[list, list] :
    """     
    检索所有大类饰品并给出名字和value值
    """
    names= bro.eles(".cols")
    name= [name.text.split() for name in names]
    value_list = []
    lis = bro.eles('css:ul.cols li')
    for li in lis:
        value = li.attr('value')
        value_list.append(value)
        logging.info(f"已获取{name}等的value")
    return name,value_list


def accessoriesurls()-> list:
    #合成所有大类的url
    accessoriesurls= []
    _,accessories_v= search() 
    for i in accessories_v:
        accessoriesurl= f"https://buff.163.com/market/csgo#game=csgo&page_num=1&category={i}&tab=selling"
        accessoriesurls.append(accessoriesurl)
        logging.info("以获取具体饰品类的网址")
    return accessoriesurls
def close():
    bro.quit()    

if __name__ == "__main__":
    open_web()
    search(bro)
    i= accessoriesurls()
    print(i)