from json import load
from os import getenv
from random import randint, choice
from time import sleep
from requests import get

bot_token = getenv("BOT_TOKEN")
chat_channel = getenv("KITI_CHAT_CHANNEL")

kiti_gifs = load(open("cat_gifs.json"))
kiti_phrases = [
    "Я нищий",
    "Хай",
    "Я люблю Маслака",
    "Саша лох",
    "Я хочу какиш"
]


def send_animation(animation_url):
    get(f"https://api.telegram.org/bot{bot_token}/sendAnimation?chat_id={chat_channel}&animation={animation_url}")

def send_message(message_text):
    get(f"https://api.telegram.org/bot{bot_token}/sendText?chat_id={chat_channel}&text={message_text}")

while 1:
    print("[=_=] Kiti neurobot started")
    roulette = randint(1, 3)
    if roulette == 1:
        print("[>_<] Kiti sends cat gif in chat")
        send_animation(choice(kiti_gifs))
    elif roulette == 2:
        print("[|_|] Kiti sends some phrase in chat")
        send_message(choice(kiti_phrases))
    else:
        print("[-_-] Kiti takes a rest")
    sleep(1)
