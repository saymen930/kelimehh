from os import getenv
from kelime_bot.config import Config
from telethon import TelegramClient
from time import sleep
import logging
from dotenv import load_dotenv, set_key, unset_key
 
 
logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)
 
 
 
api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
 
tag = TelegramClient('tag', api_id, api_hash).start(bot_token=bot_token)
 
 
