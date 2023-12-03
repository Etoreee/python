import time
import webbrowser
from datetime import datetime as dt

# Список заборонених сайтів
sites_to_block = ['www.facebook.com', 'facebook.com', 'www.youtube.com']

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
#ip
redirect = "127.0.0.1" 

def block_websites(start_hour, end_hour):
  
  while True:
    now = dt.now()
    current_time = now.strftime("%H")
    

    if start_hour < int(current_time) < end_hour:
      print("Blocking websites...")
      with open(hosts_path, 'r+') as hostfile:
        hosts_content = hostfile.read()
        for site in sites_to_block:
          if site not in hosts_content:
            hostfile.write(redirect + " " + site + "\n") 

     
    else:
      print("Unblocking websites...")
      with open(hosts_path, 'r+') as hostfile:
        lines = hostfile.readlines()
        hostfile.seek(0)  
        for line in lines:
          if not any(site in line for site in sites_to_block):
            hostfile.write(line)  
        hostfile.truncate()
        
    time.sleep(10)

if __name__ == "__main__":
  block_websites(9, 17) # час блокування з 9 до 17