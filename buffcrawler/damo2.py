#https://buff.163.com/goods/857681饰品网址
# data-goods_id="857681" 
#title="AK-47（StatTrak™） | 墨岩 (略有磨损)"
# data-goods_id="911195" 
#title="印花 | Aleksib（闪耀）| 2022年里约热内卢锦标赛"

from getAccessories import open_web,accessoriesurls
from cookie_manager import ensure_cookie



bro= open_web()


user_url= accessoriesurls()[0]#注意这样为了继续写下去先爬一个的数据

bro.change_mode()
bro.get(user_url)

details_id= bro.eles("tag=a")
for i in details_id:
    details_url= i.attr("href")
    details_name= i.attr("title")
    print(details_url,details_name) 
