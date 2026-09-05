import time
import logging
import re
from getAccessories import open_web,accessoriesurls
from config import buff_url,log_config
logging_config= log_config

bro= open_web()
bro.change_mode()
#切换模式



def into_goods(url:str)->list:
    """
    在此处拿到id未来都在这里开始搜索
    """
    goods_url= []
    bro.get(url)
    details_id= bro.eles("tag=a")
    
    for i in details_id:
        
        details_url= i.attr("href")
        goods_id = re.search(r'/goods/(\d+)', details_url)
        if goods_id:
            
            goods_url.append(goods_id.group(1))
        time.sleep(60)
        
    return goods_url
    
    
def parse_goods(page,goods_url:list)->list:
    goods = []
    
    for i in goods_url:
        
        good_url= f"https://buff.163.com/goods/{i}"    
        page.get(good_url)
        time.sleep(15)
        
        btn= page.ele("@text():成交记录")
        if btn:
            btn.click()
            page.wait(1)
        else:
            print(f"饰品 {i} 没有成交记录")
            continue

        trs = page.eles("@tag:tr")
        
        for tr in trs:
            
            try:
                
                item = {
                    "name": tr.ele("css:.textOne").text,
                    "price": tr.ele("css:.f_Strong").text,
                    "type": tr.ele('@@class=t_Left@!class=c_Gray@@tag:td').text,
                    "time": tr.ele("css:td.c_Gray").text
                }
                goods.append(item)    
                
            except AttributeError as A:
                logging.error(f"饰品 {i} 的某一行数据缺失，跳过该行。错误信息: {A}")
            
    return goods
def close():
    bro.quit() 
