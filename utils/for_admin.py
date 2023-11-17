from loader import bot
from data.config import ADMINS


async def send_message_to_admin(user_data, status):
    data_json = user_data.as_json()
    message_text = ""
    
    if status == "start":
        message_text += "Start\n"
    elif status == "send image":
        message_text += "Send image\n"

    message_text += f"{data_json}"
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text=message_text)
