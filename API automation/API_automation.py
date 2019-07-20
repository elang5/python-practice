import requests
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

PATHS = ['https://ratemusic-server.herokuapp.com/api/albums',
         'https://space-repetition-api.herokuapp.com/api/language',
         'https://laconic-api.herokuapp.com/api/videos']
current_time = datetime.now()

def automate_get_request():
  with requests.Session() as s:
    for path in PATHS:
      r = s.get(path)
      print(path)
      print(r.status_code)
      if r.status_code == 200:
        print(current_time)

scheduler = BlockingScheduler()
scheduler.add_job(automate_get_request, 'interval', minutes=1)
scheduler.start()