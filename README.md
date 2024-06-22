# snowflake-rendezvous-email-chatbot

Email bot for the snowflake project that helps conneting the proxy and the client through webRTC by forwarding the offer and answer between the broker server and the client.

## Install
pip install -r requirements.txt

## How to use

First register an email addres on the bot:
`./chatbot.py init example@domain.com PASSWORD`

Then you can run all registered email addresses:
`./chatbot.py serve`

Or you can only run one:
`./chatbot.py. --account example@domain.com serve`
