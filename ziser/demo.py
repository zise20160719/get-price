from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import requests
import time

import dingding

def job():
  printPrice()

def get(url):
  while True:
    try:
      r = requests.get(url)

    except Exception:
      time.sleep(0.5)
      continue
    if r.status_code != 200:
      time.sleep(0.5)
      continue
    r_info = r.json()
    r.close()
    return r_info


def printPrice():
  select = ['fil6zqc','omgqc']
  url = 'http://api.zb.live/data/v1/allTicker'
  for item in select:
    temp = url + "?market=" + item
    x = get(temp)
    str = ''
    for key in x:
      if key in select:
        str += '['+key+ '-' + x[key]['last'] +']\n'

  text = '测试：' +str + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  dingding.dingmessage(text=text)



if __name__ == '__main__':
  scheduler = BlockingScheduler()
  scheduler.add_job(job, 'interval', seconds=60)
  scheduler.start()