from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from pathlib import Path

bot = Bot(token=config.BOT_TOKEN, proxy=config.PROXY_URL,
          parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
BASE_DIR = Path(__file__).resolve().parent
