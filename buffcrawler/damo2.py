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

details_ids = bro.eles('[data-goods_id]')
for idetails_id in details_ids:
    details_id= idetails_id.attr("data-goods_id") 
details_title= details_ids.ele("@tag:h3")
