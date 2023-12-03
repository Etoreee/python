#встановити бібліотеку запитів#
#**********************#
#$ pip install requests#
#**********************#

import requests
import re

video_url = input("Введіть URL YouTube відео: ")

response = requests.get(video_url)
html = response.text

views = re.search(r'"viewCount":"([\d,]+)"', html)
likes = re.search(r'"videoActions":"([\d,]+)"', html)

if views:
    views = int(views.group(1).replace(",", ""))
    print(f"Перегляди: {views}")
else:
    print("Не вдалося отримати кількість переглядів")
    
if likes:
    likes = int(likes.group(1).replace(",", ""))
    print(f"Лайки: {likes}")
else:
    print("Не вдалося отримати кількість лайків")