import mysql.connector
import os
import time
from datetime import datetime
import re
import subprocess

notified = False;

while True:
    try:
        conn = mysql.connector.connect(host='database', port='3306', database='db', user='user', password='password')
        cur = conn.cursor()
        cur.execute("select number, date from number_table order by date desc limit 1")
        number, date = cur.fetchone()

        now = datetime.now()

        diff = now - date
        if diff.seconds < 15:
            process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
            process.communicate(number.encode('utf-8'))
            if not notified:
                notified = True
                subprocess.call([
                    "terminal-notifier",
                    "-group", "sms-code-to-clipboard",
                    "-title", "SMS 인증번호 클립보드에 복사됨",
                    "-message", f"인증번호 [{number}]가 클립보드에 복사되었습니다."],
                )
        else:
            notified = False;

    except Exception as e:
        print(e)
        conn = mysql.connector.connect(host='database', port='3306', database='db', user='user', password='password')
        cur = conn.cursor()
    time.sleep(0.5)
