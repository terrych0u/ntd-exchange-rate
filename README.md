# twd_exchange_rate
This is a little crawler tool for TWD exchange rate, and it will auto send info to slack if the rate have been update.

## Requirements
In order to build it you need the following python components in your system.
Which you can use "pip install", and this image will install for you.

```text
1.bs4 
2.request
3.pandas
4.slackweb
```

## Usage

Following command will help to build image  <br /> 
ex:
```bash
docker build \
--build-arg SLACK_CHANNEL_ID="123456789" \
--build-arg SLACK_CHANNEL_NAME="YOUR CHANNEL NAME" \
--build-arg CURRENCY_TYPE="JPY,USD"
-t=app .
```
**Notice: build-arg must give it, and use "," comma to separate multiple currency type.**
<br />
  
Result: 
```text
幣別: JPY，現金匯率買入/賣出: 0.2683/0.2811，即期匯率買入/賣出: 0.2756/0.2796 (牌價最新掛牌時間：2018/12/27 16:00)
幣別: USD，現金匯率買入/賣出: 30.37/31.06，即期匯率買入/賣出: 30.74/30.84 (牌價最新掛牌時間：2018/12/27 16:00)
```
