import requests
import queue
import os
from tqdm import tqdm
import threading



class downlaod:
    def __init__(self,url_list,path):
        self.url_list = url_list
        self.path = path
        self.q = queue.Queue()
        for url in self.url_list:
            self.q.put(url)
        
    
    def download1(self):
        while self.q.empty() == False:
            url = self.q.get()
            filename = os.path.basename(url)
            filename1 = filename.split("?",1)[0]
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024
            filepath = self.path + "\\" + filename1

            with open(filepath, "wb") as f:
                with tqdm(total=total_size, unit='B', unit_scale=True,desc=filename) as progress_bar:
                    for data in response.iter_content(block_size):
                        progress_bar.update(len(data))
                        f.write(data) 
        
        


class filedownloader:   # B
    def __init__(self):
        self.download_queue = queue.Queue()
        self.download_threds = []

    def add_download(self,url,path):
        self.download_queue.put((url,path))
        
    def download_worker(self):
        while True:
            try:
                url , path = self.download_queue.get(timeout = 1)
            except queue.Empty:
                print("all downloads end")
                break 
            try:   
                response = requests.get(url, stream=True)
                total_size = int(response.headers.get('content-length', 0))
                block_size = 1024
                filename1 = os.path.basename(url)
                filename = filename1.split("?",1)[0]
                filepath = f"{path}\{filename}"
                with open(filepath, "wb") as f:
                    with tqdm(total=total_size, unit='B', unit_scale=True,desc= filename) as progress_bar:
                        for data in response.iter_content(block_size):
                            progress_bar.update(len(data))
                            f.write(data)
            except Exception as e:
                print(f"Eroor: {e}")

            self.download_queue.task_done()
    def start(self,treds_number = 2):
        for i in range(treds_number):
            thred = threading.Thread(target = self.download_worker)
            thred.start()
            self.download_threds.append(thred)
