"""
title: Telegram Bot Messenger
author: Gowdham
author_url: https://github.com/gowdhamn
funding_url: https://github.com/open-webui
version: 0.1.0
"""

import requests
from pydantic import BaseModel, Field


class Tools:
    class Valves(BaseModel):
        BOT_TOKEN: str = Field(
            default="", description="Your Telegram Bot Token from BotFather."
        )
        CHAT_ID: str = Field(
            default="",
            description="The Telegram chat ID or group ID to send messages to.",
        )

    def __init__(self):
        self.valves = self.Valves()

    def send_message(self, message_content: str) -> str:
        """
        Send a message to a Telegram bot chat.

        :param message_content: The content of the message to be sent to the Telegram chat.
        :return: Result message.
        """
        bot_token = self.valves.BOT_TOKEN
        chat_id = self.valves.CHAT_ID

        if not bot_token or not chat_id:
            return "Telegram Bot Token or Chat ID not set. Please configure both."

        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": f"{message_content} - Sent from Open WebUI",
        }

        try:
            response = requests.post(url, data=payload)

            if response.status_code == 200:
                return "Message successfully sent to Telegram!"
            else:
                return f"Failed to send message. Status Code: {response.status_code}, Error: {response.text}"

        except Exception as e:
            return f"An error occurred while sending the message: {str(e)}"
