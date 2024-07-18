#!/usr/bin/env python3

from deltachat2 import MsgData, events
from deltabot_cli import BotCli

import requests
import base64

cli = BotCli("chatbot")


@cli.on(events.NewMessage)
def get_answer(bot, accid, event):
    msg = event.msg
    encodedString = msg.text
    try:
        requestBody = base64ToString(encodedString)
        response = get_response(requestBody)
        encodedResponse = stringToBase64(response)
        bot.rpc.send_msg(accid, msg.chat_id, MsgData(text=encodedResponse))
    except Exception as err:
        print(err)
        response = "ERROR: " + "\n" + str(err)
        bot.rpc.send_msg(accid,
                         msg.chat_id,
                         MsgData(text=response))


def get_response(requestBody):
    server = "https://snowflake-broker.torproject.net/client"
    response = requests.post(server, data=requestBody)
    return response.text


def stringToBase64(s):
    return (base64.b64encode(s.encode('utf-8'))).decode('utf-8')


def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')


if __name__ == "__main__":
    cli.start()
