from datetime import datetime
import time
import os



LOGS = os.path.join('static', 'logs')


class Times:
    localtime = lambda:datetime.now()
    timestamp = lambda:int(time.time())
    timestr = lambda:datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]


class WebIP:
    HOST = '*'
    PORT = 4242


