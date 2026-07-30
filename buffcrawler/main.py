from market_crawler import user_url
from sql import matter_sql

main_data,goods_name  = user_url()

if __name__ == "__main__":
    matter_sql()
#pip install -r requirements.txt