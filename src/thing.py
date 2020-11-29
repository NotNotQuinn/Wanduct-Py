from util.parser import parsemsg
import socket
import json
import time
import logging

logger = logging.Logger(name="thing.py",level=logging.DEBUG)
logging.basicConfig(
            level=logging.DEBUG, 
            format=f'[%(asctime)s] [%(name)s] [%(levelname)-8s] - %(message)s'
    )


with open('/mnt/c/dev/py/wanduct/src/oauth.json') as f:
    oauth_token = str(json.load(f)[0])

conn = socket.socket()
def send_raw(text: str):
    conn.send(bytes(f"{text}\r\n",'utf-8'))
    logging.debug(f'Sending raw: {text}')


conn.connect(('irc.chat.twitch.tv', 6667)) 
send_raw(f'PASS {oauth_token}')
send_raw("NICK quinndt")

channels = [
    "#quinndt",
    "#turtoise",
    "#michaelreeves"
]

for channel in channels:
    send_raw(f"JOIN {channel}")
send_raw('CAP REQ :twitch.tv/tags')
loop = True

while loop:
    data = conn.recv(2048).decode('utf-8')

    data2 = data.splitlines()
    for message in data2:
        (prefix, command, args, tags) = parsemsg(message)
        logging.info(f"Raw: {message}")
        logging.info(f"Prefix: {prefix}")
        logging.info(f"Command: {command}")
        logging.info(f"Args: {str(args)}")
        logging.info(f"Tags: {tags}")
        if command == "PING":
            send_raw(f"PONG :{args[0]}")
        if command == "PRIVMSG":
            if tags['display-name'] == "QuinnDT" and \
                args[1].split(' ')[0].lower() == '!' and \
                tags['mod'] == '1':
                send_raw(f"PRIVMSG {args[0]} :/delete {tags['id']}")
