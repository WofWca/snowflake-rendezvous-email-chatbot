# snowflake-rendezvous-email-chatbot

Email chatbot for the snowflake project that helps conneting the proxy and the client through webRTC by forwarding the offer and answer between the broker server and the client.

## Install
```
pip install -r requirements.txt
```

## How to use
First register an email addres on the bot:
```
./chatbot.py init example@domain.com PASSWORD
```

Then you can run all registered email addresses:
```
./chatbot.py serve
```

Or you can only run one:
```
./chatbot.py. --account example@domain.com serve
```
## Test
[Click to test](mailto:example@domain.com?body=1.0%0A%7B%22offer%22%3A%22%7B%5C%22sdp%5C%22%3A%5C%22v%3D0%5C%5Cr%5C%5Cno%3D-%208955625195614447027%202%20IN%20IP4%20127.0.0.1%5C%5Cr%5C%5Cns%3D-%5C%5Cr%5C%5Cnt%3D0%200%5C%5Cr%5C%5Cna%3Dgroup%3ABUNDLE%200%5C%5Cr%5C%5Cna%3Dextmap-allow-mixed%5C%5Cr%5C%5Cna%3Dmsid-semantic%3A%20WMS%5C%5Cr%5C%5Cnm%3Dapplication%2012087%20UDP%2FDTLS%2FSCTP%20webrtc-datachannel%5C%5Cr%5C%5Cnc%3DIN%20IP4%20152.206.187.234%5C%5Cr%5C%5Cna%3Dcandidate%3A735233449%201%20udp%202113937151%2010.53.196.43%2043502%20typ%20host%20generation%200%20network-cost%20999%5C%5Cr%5C%5Cna%3Dcandidate%3A60734312%201%20udp%201677729535%20152.206.187.234%2012087%20typ%20srflx%20raddr%2010.53.196.43%20rport%2043502%20generation%200%20network-cost%20999%5C%5Cr%5C%5Cna%3Dice-ufrag%3AKiO0%5C%5Cr%5C%5Cna%3Dice-pwd%3AXyDW3je%2BiOVV%2Fo6%2FNxf2acir%5C%5Cr%5C%5Cna%3Dice-options%3Atrickle%5C%5Cr%5C%5Cna%3Dfingerprint%3Asha-256%2081%3A18%3AD1%3AE8%3A5A%3A43%3A2A%3A4A%3ADE%3ABA%3A21%3A6E%3A47%3A0C%3A64%3A19%3A44%3AB4%3A22%3AFE%3AC0%3A64%3AC9%3A4C%3A1C%3AEE%3A9B%3ABF%3A42%3A1A%3A7A%3AB7%5C%5Cr%5C%5Cna%3Dsetup%3Aactpass%5C%5Cr%5C%5Cna%3Dmid%3A0%5C%5Cr%5C%5Cna%3Dsctp-port%3A5000%5C%5Cr%5C%5Cna%3Dmax-message-size%3A262144%5C%5Cr%5C%5Cn%5C%22%2C%5C%22type%5C%22%3A%5C%22offer%5C%22%7D%22%2C%22nat%22%3A%22unrestricted%22%2C%22fingerprint%22%3A%222B280B23E1107BB62ABFC40DDCC8824814F80A72%22%7D)
