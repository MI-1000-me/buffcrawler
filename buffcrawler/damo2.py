#https://buff.163.com/goods/857681饰品网址
# data-goods_id="857681" 
#title="AK-47（StatTrak™） | 墨岩 (略有磨损)"
# data-goods_id="911195" 
#title="印花 | Aleksib（闪耀）| 2022年里约热内卢锦标赛"
from DrissionPage import Chromium
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
from DrissionPage.common import Settings
from DrissionPage.common import By

from getAccessories import open_web, search
from cookie_manager import ensure_cookie

bro= open_web()
_,accessories_v= search()
