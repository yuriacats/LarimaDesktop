# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import eel
import sqlite3
import os
from tkinter import filedialog, Tk
import datetime
import platform
import schedule
import time
from plyer import notification
import random
import requests
from bs4 import BeautifulSoup



def larima_tell(message: str):
    if platform.system()== "Darwin":
        os.system("osascript -e 'display notification\" {}\"'".format(message))
    else:
        notification.notify(title='Rima', message='message')


def job():
    msgList = [
    "ねーねー。",
    "きいてるー？？",
    "はなそーよー",
    "大好きだよ",
    "愛してるよー！",
    "すき……",
    "ちゅっちゅ！！",
    "他の女と一緒にいないよね…？",
    "あなたを誰にも渡さない……",
    "ねー……",
    "むぅ",
    "いっぱいお話したいだけなのに……",
    "ねぇってばー",
    "すきだよ？",
    "こんなに好きなのに……",
    "私が悪いのかな……?",
    "はぁ。。。",
    "ふーん…",
    "こんなにすきなのに……",
    "あいたい。",
    "ねぇ、会いたいよー……",
    "通話しよ。。。",
    ]

    return 0


def get_news():
    # ここで、虚構新聞からニュースをスクレイピングする
    kyoko_url = 'https://kyoko-np.net/entertainment.html'
    news_list = news_parser(kyoko_url, "h4")
    return news_list[random.randint(0, len(news_list)-2)]


def news_parser(url: str, tag: str = "li"):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    return list(map(lambda x: x.get_text(strip=True), soup.select(tag)))


def call_wait():
    schedule.every(10).seconds.do(larima_tell,"ねえねえ、こんなニュースがあったよ！「"+get_news()+"」")
    #schedule.every().day.at("7:00").do(larima_tell("ねえねえ、こんなニュースがあったよ！「"+get_news()+"」"))
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            print("中断しました。")
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    call_wait()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
