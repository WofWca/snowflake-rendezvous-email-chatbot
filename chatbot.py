#!/usr/bin/env python3

from deltachat2 import MsgData, events
from deltabot_cli import BotCli

import requests
import json

cli = BotCli("chatbot")


@cli.on(events.NewMessage)
def get_response(bot, accid, event):
    msg = event.msg
    try:
        clientData = json.loads(msg.text)
        answer = get_answer(clientData)
        bot.rpc.send_msg(accid, msg.chat_id, MsgData(text=answer))
    except Exception as err:
        print(err)
        answer = "ERROR: " + "\n" + str(err)
        bot.rpc.send_msg(accid,
                         msg.chat_id,
                         MsgData(text=answer))


def get_answer(clientData):
    clientVersion = clientData["clientVersion"]
    server = clientData["server"]
    fingerprint = clientData["fingerprint"]
    nat = clientData["nat"]
    offer = clientData["offer"]

    body = (
        clientVersion
        + "\n"
        + json.dumps({"offer": json.dumps(offer),
                      "nat": nat,
                      "fingerprint": fingerprint})
    )

    resp = requests.post(server, data=body)
    answer = resp.text
    return answer


if __name__ == "__main__":
    cli.start()
