#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from requests_html import HTMLSession

url = "http://rate.bot.com.tw/xrt?Lang=zh-TW"

session = HTMLSession()
r = session.get(url)

e = r.html.find("class#time", first=True)
# print(r.html.html)
print(r.html.xpath("//span[@class='time']/text()"))
