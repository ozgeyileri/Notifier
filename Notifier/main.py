import time

from pync import Notifier

title = 'Hi , Hello and Hi!'
message = 'I LOVE YOU'
Notifier.notify(title=title, message=message,app_icon="heart.png" , timeout=15, toast=False)

time.sleep(60*60)