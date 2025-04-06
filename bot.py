from pyrogram import Client, filters, types
import yaml
import os

from handlers.start_handler import start_hanle
from handlers.help_handler import help_handle

# Перевірка наявності тестового конфігураційного файлу
config_path = "config/test_config.yml" if os.path.exists("config/test_config.yml") else "config/config.yml"

# Завантаження конфігурації з файлу
with open(config_path, 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

app = Client(
    "DrunkenBerryBot",
    api_id=config["API_ID"],
    api_hash=config["API_HASH"],
    bot_token=config["BOT_TOKEN"]
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await start_hanle(client, message)

@app.on_message(filters.command("help"))
async def help_command(client, message):
    await help_handle(client, message)

app.run()
