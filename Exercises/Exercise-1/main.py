import requests
from io import BytesIO
import os 
import zipfile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

output_dir = '/Users/dita/Documents/Personals Projects/data-engineering-practice/Exercises/Exercise-1/output/'
def main():
    # your code here
    os.makedirs(output_dir, exist_ok=True)

    for i in download_uris:
        filename = i.split("/")[-1]
        filepath = os.path.join(output_dir,filename)
        print(f"{filename} already downloaded")
        response = requests.get(i)

        if response.status_code==200:
            with zipfile.ZipFile(BytesIO(response.content)) as zf:
                zf.extractall(output_dir)
                print("finish all")
        else:
            print("failed")


if __name__ == "__main__":
    main()
