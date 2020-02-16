import datetime as dt
import os
import time


def conditional_shutdown():
    while True:
        time.sleep(60)
        day = dt.date.today().isoweekday()
        timenow = dt.datetime.now().hour
        if day == 5:
          if timenow < 5:
              os.system('shutdown -s -t 1')
          else:
              pass
        elif day == 6 or day == 7:
            if timenow < 5:
                os.system('shutdown -s -t 1')
            else:
                pass
        elif day == 7:
            if timenow >= 23:
                os.system('shutdown -s -t 1')
            else:
                pass
        else:
            if timenow >= 23 or timenow < 5:
                os.system('shutdown -s -t 1')
            else:
                pass
        time.sleep(540)


conditional_shutdown()
