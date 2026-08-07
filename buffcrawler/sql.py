import pymysql

from main import main_data,goods_name 

bata = main_data
def open_sql(func):
    def a():
        conn = pymysql.connect(
            host='localhost',       # 地址
            port=3306,              # 端口
            user='   ',            # 用户名
            password='   ',      # 密码
            database='buffcrawlerbase',# 数据库名
            charset='utf8mb4'       # 字符集
        )
        cursor = conn.cursor()
        func(cursor)
        conn.commit()
        conn.close()
    return a
#---代码写这-----
@open_sql
def matter_sql(cursor):
    for name in goods_name:
        good_data= bata[name]
        
        for item in good_data:
            
            good_name= item['name']
            good_price= item['price']
            good_type= item['type']
            good_time= item['time']
            
            cursor.execute(
            "INSERT INTO goods (good_name, good_price,good_type,good_time) VALUES (%s, %s, %s, %s)",   # ← SQL 模板
            (
                good_name,
                good_price,
                good_type,
                good_time
            )                        
                )
#---------------

