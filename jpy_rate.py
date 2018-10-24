#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import re
import requests
import slackweb
from BeautifulSoup import BeautifulSoup


def remove_tags(text):
    tag_re = re.compile(r'<[^>]+>')
    return tag_re.sub('', str(text))

def send_slack(p1,p2,p3,p4,times):
    slack = slackweb.Slack('https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXX')
    slack.notify(text="現金匯率買入/賣出 "+p1+"/"+p2+"，即期匯率買入/賣出 "+p3+"/"+p4+" (牌價最新掛牌時間："+times+")" ,channel="#jpy_rate",username="jpy_rate_bot")

def write_times(times):
    f = open("/tmp/jpy_rate", "w")
    f.write(times)
    f.close()
  

cashs=[]
sights=[]

soup = BeautifulSoup(requests.get("http://rate.bot.com.tw/xrt?Lang=zh-TW").text)
cash_data = soup.findAll("td", {'class': 'rate-content-cash text-right print_hide'})
sight_data = soup.findAll("td", {'class': 'rate-content-sight text-right print_hide'})
times = soup.findAll("span", {'class': 'time'})
times = remove_tags(times[0])

for cash in cash_data:
    cashs.append(remove_tags(cash))

for sight in sight_data:
    sights.append(remove_tags(sight))

if os.path.exists("/tmp/jpy_rate"):
    f = open("/tmp/jpy_rate", "r")
    old_times = f.read().strip()
    f.close()

    if old_times != times : 
        send_slack(cashs[14],cashs[15],sights[14],sights[15],times)
        write_times(times)
    else :
        exit()
else :
    send_slack(cashs[14],cashs[15],sights[14],sights[15],times)
    write_times(times)

