import requests
import json

import requests

url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

querystring = {"url":"https://www.instagram.com/p/CbXzHzEFv5q/"}

headers = {
	"X-RapidAPI-Key": "7f3e694761mshec679b5f0557f9cp142cb2jsn59b13828e70e",
	"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())