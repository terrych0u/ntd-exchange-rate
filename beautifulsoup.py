#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os
import requests
import slackweb
import sys
import time
import pandas as pd



slack_channel_id = os.environ['SLACK_CHANNEL_ID_ENV']
slack_channel_name = os.environ['SLACK_CHANNEL_NAME_ENV']
target_type = os.environ['CURRENCY_TYPE_ENV'].split(',')

url = "http://rate.bot.com.tw/xrt?Lang=zh-TW"
last_time = ""



def send_slack(contents):
    for x in zip(*[iter(contents)]*len(contents)):
        message = '幣別: {0}，現金匯率買入/賣出: {1}/{2}，即期匯率買入/賣出: {3}/{4} (牌價最新掛牌時間：{5})' .format(*x)
    # print(message)
    slack = slackweb.Slack('https://hooks.slack.com/services/'+slack_channel_id)
    slack.notify(text=message, channel=slack_channel_name, username="exchange_rate_bot")



if __name__ == '__main__':

    while True:
        try:
            resp = requests.get(url, timeout=3)
        except:
            print ("Connect failed, Please help to check web page status")
            sys.exit(1)

        soup = BeautifulSoup(resp.text, 'html.parser')


        raw_time = soup.find("span", {'class': 'time'})
        times = BeautifulSoup(str(raw_time), features="lxml")

        if times.span.string != last_time:

            dfs = pd.read_html(resp.text)
            currency = dfs[0]  
            currency = currency.iloc[:, 0:5]
            currency.columns = [u'Type', u'cashs-bank_buy',
                                u'cashs-bank_sell', u'spot-bank_buy', u'spot-bank_sell']
            currency[u'Type'] = currency[u'Type'].str.extract('\((\w+)\)')

            for i in target_type:
                try:
                    contents = currency.loc[currency['Type'] == i].values[0]
                    message = list(contents)
                    message.append(times.span.string)
                except:
                    print("Currency type can't find, Please check the type you input")
                    sys.exit(1)

                send_slack(message)

            last_time = times.span.string
            
        else:
            time.sleep(5)
