# Task 4

# Download links.parquet from https://drive.google.com/file/d/1ym_RbsjN41cwXZLeB3NibN7h7Vbz1AgP/view?usp=sharing

# Download and save the first 10,000 images from the links in the parquet file.

# - Monitor CPU and network usage during download.

# References:
# pyarrow package
# requests package

import pyarrow.parquet as pq
import requests
import os
file_path = "task_4\links.parquet"
df = pq.read_table(source =file_path, columns=["URL"]).to_pandas()

def download_image(url,index,folder_path ="task_4\downloads" ):
    image_path = f"image__{index}.png"
    image_path = os.path.join(folder_path,image_path)
    try:
        response = requests.get(url=url)
        if response.status_code == 200:
            with open(image_path,'wb') as file:
                file.write(response.content)
                print(image_path,"Saved")
    except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    n = int(input("Enter the number of files to download : "))
    i=0
    for index , url in df ["URL"].items():
        if(i==n):
            break
        else:
            download_image(url,index)
            i+=1
            
