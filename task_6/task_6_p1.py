# Task 6

# Part 1:
# Optimize download speeds in Downloader class by using threads.
# Monitor CPU usage and time taken.

# References:
# concurrent.futures.ThreadPoolExecutor

import pyarrow.parquet as pq
import os
import requests
from concurrent.futures import ThreadPoolExecutor

class Downloader:
    def __init__(self,pq_file:str):
        self.df = pq.read_table(source = pq_file, columns=["URL"]).to_pandas()
        self.executor = ThreadPoolExecutor(max_workers=80)

    def __getitem__(self,key):
         if isinstance(key,int):
             path = self.download_image(key)
         elif isinstance(key,slice):
             start = key.start
             stop = key.stop
             path = self.download_images(start,stop+1)
         return path
    def download_image(self,index: int,folder_path ="../downloads/imgs" ):
        url = self.df.iloc[index]["URL"]
        print(url)
        os.makedirs(folder_path,exist_ok=True)
        URL = url.split("/")[-1]
        extension = URL.split("?")[0]
        file_type = extension.split(".")[-1]
        if(file_type==""):
            file_type="png"
        image_path = f"image_{index}.{file_type}"
        image_path = os.path.join(folder_path,image_path)
        try:
            response = requests.get(url=url)
            if response.status_code == 200:
                with open(image_path,'wb') as file:
                    file.write(response.content)
                    print(image_path,"Saved")
                    return image_path
            else:
                print(f"Failed to download {url}, status code: {response.status_code}")
        except Exception as e:
                print(f"An error occurred: {e}")
        return "Download Failed!"
    def download_images(self,start:int,stop:int):
        img_paths=[]
        futures = []
        for i in range(start,stop):
            future = self.executor.submit(self.download_image,i)
            futures.append(future)
        for future in futures:
            img_path = future.result()
            img_paths.append(img_path)
        return img_paths

  
# Driver code 
file_path = "../downloads/links.parquet"
if __name__ == "__main__":
    test = Downloader(file_path) 
    path = test[5]
    path2 = test[5:2000] 



