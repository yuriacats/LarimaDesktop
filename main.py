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



def larima_tell(message: str,now_time: str):
    msg="Rima:["+now_time+"]"+message
    if platform.system()== "Darwin":
        os.system("osascript -e 'display notification\" {}\"'".format(msg))
    else:
        notification.notify(title='Rima', message='message')


def job(ofen):
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
    job_id=random.randint(0,len(msgList)+ofen)
    dt_now = datetime.datetime.now()
    now_time=dt_now.strftime('%H:%M:%S')
    now_date=dt_now.strftime('%Y-%m-%d/')

    if job_id<len(msgList):
        #print(now_time)
        white_sql(msgList[job_id], now_date, now_time,0)
        larima_tell(msgList[job_id],now_time)
    elif job_id<len(msgList)+4:
        #print(now_time)
        white_sql("ねえねえ、こんなニュースがあったよ！「"+get_news()+"」",now_date,now_time,0)
        larima_tell("ねえねえ、こんなニュースがあったよ！「"+get_news()+"」",now_time)
    return 0


def white_sql(message: str, now_date: str , now_time: str, from_user: int = 0):
    connection = sqlite3.connect('chat.db',isolation_level=None)
    cur=connection.cursor()
    cur.execute( """CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY UNIQUE,
        from_user INTEGER ,
        message TEXT ,
        date TEXT ,
        time TEXT
        ) """)
    cur.execute("INSERT INTO messages (from_user, message,date,time) VALUES (?,?,?,?)", (from_user, message,now_date,now_time))
    connection.close()
    return message,now_time


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
    schedule.every(1).seconds.do(job,100)
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
