import numpy as np
import pandas as pd
import requests
import json

url = "https://www.reliancedigital.in/rildigitalws/v2/rrldigital/storelocator/storedata"

payload = json.dumps({
  "city": "",
  "format": "DIGITAL;JIO STORE;DX MINI;DIGITALRESQ",
  "latitude": 20.5937,
  "longitude": 78.9629,
  "radius": 10000
})
headers = {
  'authority': 'www.reliancedigital.in',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'origin': 'https://www.reliancedigital.in',
  'referer': 'https://www.reliancedigital.in/locateus',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

store_Name=[]
address=[]
timings=[]
latitude=[]
longitude=[]
phone_number=[]
response = requests.request("POST", url, headers=headers, data=payload).json()
stores = response["stores"]
for i in stores:
    store_Name.append(i["storeName"])
    address.append(i["address"])
    timings.append(i["storeTime"])
    latitude.append(i["latitude"])
    longitude.append(i["longitude"])
    phone_number.append(i["storeStaffMobile1"])
    
dic={"Store_Name":store_Name,"Address":address,"Timings":timings,"Latitude":latitude,"Longitude":longitude,"Phone_number":phone_number}
df=pd.DataFrame(dic)
df.to_csv("D:/python exersice/pandas/reliance_retail_stores.csv",)
print(df)

    


