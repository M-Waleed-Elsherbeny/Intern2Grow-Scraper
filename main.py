import requests
import json


URL = "https://intern2grow.vercel.app/programs"
URL_API = "https://intern2grow.vercel.app/api/programs"

HEADERS = {
    "Accept-Language": "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,hy;q=0.6",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}
response = requests.get(URL_API)
response.raise_for_status()

all_data = response.json()

all_info = {}
for data in all_data:
    all_info.update({
        data["slug"]: {
        "title": data["title"],
        "describtion": data["responsibilities"],
        "skills": data["skills"],
        }})

with open("all_programmes.json", "w") as f:
    json.dump(all_info, f, indent=4)
    print("Success")
        
        


