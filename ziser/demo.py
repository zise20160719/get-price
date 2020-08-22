from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import requests
import time

import dingding

def job():
  print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
  printPrice()

def get():
  url = 'http://api.zb.live/data/v1/allTicker'
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
  x = get()
  select = ['fil6zqc','omgqc']
  str = ''
  for key in x:
    if key in select:
      str += '\n['+key+ '-' + x[key]['last'] +']'
      print(key, x[key])

  text = '测试：\n' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +str
  dingding.dingmessage(text=text)



if __name__ == '__main__':
  scheduler = BlockingScheduler()
  scheduler.add_job(job, 'interval', seconds=60)
  scheduler.start()