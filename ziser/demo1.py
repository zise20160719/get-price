import requests
import time

def get( url):
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

def getTicker(ticker):
  url = 'http://api.zb.live/data/v1/ticker?market=' + ticker
  return get(url)

if __name__ == '__main__':
    ticker = getTicker('fil6z_qc')
    print(ticker)
