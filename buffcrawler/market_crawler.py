import re

from getAccessories import open_web,accessoriesurls,search
from goods_detail import into_goods,parse_goods




def user_url(bro):
    
    bro= open_web()
    
    data = {}

    goods_name = search(bro)          # 获取饰品名字
    all_goods_url = accessoriesurls() # 获取饰品分类url


    for name, category_url in zip(goods_name, all_goods_url):

        all_goods_ids = []

        for page in range(1, 100):

            url = re.sub(
                r'page_num=\d+',
                f'page_num={page}',
                category_url
            )
            
            try:
                goods_ids = into_goods(url)

            except Exception as e:
                print(f"{name} 第{page}页失败:", e)
                continue

            if not goods_ids:
                break

            all_goods_ids.extend(goods_ids)
        goods = parse_goods(bro,all_goods_ids)
        
        data[name] = goods

    return data
