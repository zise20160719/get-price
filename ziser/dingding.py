import json

import requests


def dingmessage(text):
  # 请求的URL，WebHook地址
  webhook = "https://oapi.dingtalk.com/robot/send?access_token=eb881c7e9c5018d1827c08db3da24c75a1ec8a7eca3e42a39f33643f0a8ff42e"
  # 构建请求头部
  header = {
    "Content-Type": "application/json",
    "Charset": "UTF-8"
  }
  # 构建请求数据
  tex = text
  message = {
    "msgtype": "text",
    "text": {
      "content": tex
    },
    "at": {
      "isAtAll": True
    }

  }
  # 对请求的数据进行json封装
  message_json = json.dumps(message)
  # 发送请求
  info = requests.post(url=webhook, data=message_json, headers=header)
  # 打印返回的结果
  print(info.text)


if __name__ == "__main__":
  dingmessage()
