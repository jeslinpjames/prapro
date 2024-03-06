# Create a class Downloader with the following template:

# class Downloader:
#     ...
#     def __init__(self, pq_file: str):
#         ...

# where pq_file is the path to the parquet file.

# At the end of the task, the following things should work on an instance of Downloader called d:

# d[i] will download the i'th image and return its local path
# d[i : j] will download i to j images and return their local paths in a list

import pyarrow.parquet as pq
import os
import requests

class Downloader:
    def __init__(self,pq_file:str):
        self.df = pq.read_table(source = pq_file, columns=["URL"]).to_pandas()

    def __getitem__(self,key):
         if isinstance(key,int):
             path = self.download_image(key)
         elif isinstance(key,slice):
             start = key.start
             stop = key.stop
             path = self.download_images(start,stop+1)
         return path
    def download_image(self,index: int,folder_path ="task_4\downloads" ):
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
            else:
                print(f"Failed to download {url}, status code: {response.status_code}")
        except Exception as e:
                print(f"An error occurred: {e}")
        return image_path
    def download_images(self,start:int,stop:int):
        img_paths=[]
        for i in range(start,stop):
            img_path = self.download_image(i)
            img_paths.append(img_path)
        return img_paths

  
# Driver code 
file_path = "task_4\links.parquet"
test = Downloader(file_path) 
path = test[5]
path2 = test[5:10] 



