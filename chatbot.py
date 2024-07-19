#!/usr/bin/env python3

from deltachat2 import MsgData, events
from deltabot_cli import BotCli

import requests
import base64

cli = BotCli("chatbot")


@cli.on(events.NewMessage)
def get_answer(bot, accid, event):
    msg = event.msg
    try:
        try:
            requestBody = base64ToString(msg.text)
        except Exception:
            requestBody = msg.text

        response = get_response(requestBody)

    except InvalidDataException:
        response = "ERROR: " + "\n" + "Invalid data"
    except Exception as err:
        print(err)
        response = "ERROR: " + "\n" + str(err)

    bot.rpc.send_msg(accid, msg.chat_id, MsgData(text=response))


def get_response(requestBody):
    server = "https://snowflake-broker.torproject.net/client"
    response = requests.post(server, data=requestBody)
    status = response.status_code
    if status != 200:
        raise InvalidDataException
    return response.text


def base64ToString(b):
    return base64.b64decode(b).decode("utf-8")


class InvalidDataException(Exception):
    """Invalid data"""


if __name__ == "__main__":
    cli.start()
