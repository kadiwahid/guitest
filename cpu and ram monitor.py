import psutil
import time

def dispaly_percentage(bar = 25):
    while True:
        cpu_usage  = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent 
        cpu_percent = (cpu_usage / 100.0)
        mem_percent = (ram_usage / 100.0)
        
        cpu_bar = "=" * int(cpu_percent * bar) + "-" * (bar - int(cpu_percent * bar))
        mem_bar = "=" * int(mem_percent * bar) + "-" * (bar - int(mem_percent * bar))
        print(f"\r CPU Usage: |{cpu_bar}| {cpu_usage}%   " ,end = "")
        print(f" RAM Usage: |{mem_bar}| {ram_usage}%  \r ",end = "")
        time.sleep(0.5)


dispaly_percentage()
 

