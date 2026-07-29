from DrissionPage import Chromium
from DrissionPage import ChromiumOptions
from DrissionPage.common import Settings
from pathlib import Path


from cookie_manager import ensure_cookie

co = ChromiumOptions()
co.headless(True)  # 无头模式
co.no_imgs(True)   # 禁用图片
co.incognito()     # 无痕模式



manager = ensure_cookie()  
url= "https://buff.163.com/market/csgo#game=csgo" 
Settings.set_language('zh_cn')
bro= Chromium(addr_or_opts=co).latest_tab


def open_web(): 
    bro.set.user_agent( 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36')
    bro.set.cookies(manager.cookie)
    bro.get(url)
    return bro

        
def search(bro):
    names= bro.eles(".cols")
    name= [name.text.split() for name in names]
    value_list = []
    #注意一个种类结束link.link是none
    # value
    lis = bro.eles('css:ul.cols li')
    for li in lis:
        value = li.attr('value')
        value_list.append(value)
    return name,value_list


def accessoriesurls():
    accessoriesurls= []
    _,accessories_v= search()  #大脑枯竭了，这个变量接受的是饰品类的id吧，就是下面用的那个
    for i in accessories_v:
        accessoriesurl= f"https://buff.163.com/market/csgo#game=csgo&page_num=1&category={i}&tab=selling"
        accessoriesurls.append(accessoriesurl)
    return accessoriesurls
def close():
    bro.quit()    

if __name__ == "__main__":
    open_web()
    search(bro)
    i= accessoriesurls()
    print(i)