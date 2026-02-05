import os
import time
from datetime import datetime


HTML = os.path.join('static', 'html')
DIST = os.path.join('static', 'dist')
LOGS = os.path.join('static', 'logs')
IMGS = os.path.join('static', 'image')

class WebIP:
    HOST = '0.0.0.0'
    PORT = 5015

class Times:
    localtime = lambda:datetime.now()
    timestamp = lambda:int(time.time())
    timestr = lambda:datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]