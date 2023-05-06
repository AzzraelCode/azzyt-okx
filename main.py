from bot.Logger import setup_logger
logger = setup_logger()

from okx.exceptions import OkxAPIException
from bot import Bot

from dotenv import load_dotenv
# load_dotenv() # чтобы использовать .env рядом с main.py
load_dotenv('hidden/.env_demo', override=True) # а эту строку удали

if __name__ == '__main__':
    try:
        Bot().run()
    except KeyboardInterrupt as e:
        logger.debug("Бот остановлен вручную!")
    except OkxAPIException as e:
        logger.debug(str(e))
    except Exception as e:
        logger.error(str(e))
