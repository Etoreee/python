import os
# Скачати бібліотеку PyTube: pip install pytube
from pytube import YouTube


DEFAULT_PATH = os.path.join(os.path.expanduser('~'), 'Downloads')

def download_video(link, path=DEFAULT_PATH):
  try:
    yt = YouTube(link)

  except Exception as e:
    print("Помилка отримання даних відео", e)

  try:
    stream = yt.streams.get_highest_resolution()

    print(f"Завантаження {yt.title}...")
    stream.download(output_path=path)
    print(f"{yt.title} завантажено успішно в {path}")

  except Exception as e:
    print("Помилка завантаження відео", e)  


if __name__ == "__main__":
  # Приклади шляхів для Windows та Linux
  windows_path = "C:/Users/Max/Videos"
  linux_path = "/home/max/videos"

  link = input("Введіть посилання: ")

  # Якщо користувач не ввів, буде в папку Downloads
  path = input("Введіть повний шлях (Enter для за замовчуванням): ") 
  if not path:
    path = DEFAULT_PATH
  
  download_video(link, path)