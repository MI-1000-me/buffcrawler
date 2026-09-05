import logging
buff_url= "https://buff.163.com/market/csgo#game=csgo"

log_config= logging.basicConfig(
                    level=logging.INFO,
                    format="%(levelname)s - %(asctime)s - %(funcName)s - %(message)s",
                     datefmt="%Y-%m-%d %H:%M:%S",
                     filename="cookies.log",
                     filemode="a",
                     encoding= "utf-8",
                     )
