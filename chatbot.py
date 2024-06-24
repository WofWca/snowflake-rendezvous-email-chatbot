#!/usr/bin/env python3

from deltachat2 import MsgData, events
from deltabot_cli import BotCli

import requests

cli = BotCli("chatbot")


@cli.on(events.NewMessage)
def get_answer(bot, accid, event):
    msg = event.msg
    try:
        requestBody = msg.text
        response = get_response(requestBody)
        bot.rpc.send_msg(accid, msg.chat_id, MsgData(text=response))
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


if __name__ == "__main__":
    cli.start()
