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

def larima_gui():
    return 0


def larima_tell(message: str):
    if platform.system()== "Darwin":
        os.system("osascript -e 'display notification\" {}\"'".format(message))
    else:
        notification.notify(title='Rima', message='message')


def job():
    # ここでデータベースを読み込んで現在の時間と照らし合わせる
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
    schedule.every(10).seconds.do(job)
    schedule.every().day.at("7:00").do(get_news)
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            print("中断しました。")
            break
    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    larima_tell("test")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
