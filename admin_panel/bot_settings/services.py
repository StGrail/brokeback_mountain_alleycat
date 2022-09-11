from typing import Union

import requests

from core import settings


class TelegramApiRequest:

    _api_url = settings.TG_API
    _bot_token = settings.BOT_TOKEN

    def __init__(
            self,
            chat_ids: Union[list, str],
            message: str,
            keyboard: str = None,
    ):
        self.chat_ids = chat_ids
        self.message = message
        self.keyboard = keyboard
        self.request_url = f'{self._api_url}bot{self._bot_token}/'

    def send_message_to_users(self) -> None:
        url = self.request_url + 'sendMessage'
        for chat_id in self.chat_ids:
            query_params = {'chat_id': str(chat_id), 'text': self.message}

            requests.get(
                url,
                params=query_params,
            )

    def send_message_to_users_with_keyboard(self) -> None:
        url = self.request_url + 'sendMessage'
        for chat_id in self.chat_ids:
            query_params = {'chat_id': str(chat_id), 'text': self.message, 'reply_markup': self.keyboard}

            requests.get(
                url,
                params=query_params,
            )
