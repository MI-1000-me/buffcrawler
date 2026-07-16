import json

from DrissionPage import SessionPage
from DrissionPage import Chromium

bro= Chromium().latest_tab
cookie_list= []

def getCookie(url):
    bro.get(url)
    user_cooikes= bro.cookies()
    cookie_list.append(user_cooikes)
    return user_cooikes


def store_cookie():
    with open("cookie.json","w",encoding="utf8")as cooi:
        json.dumps(cookie_list)
        

