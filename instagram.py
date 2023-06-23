import requests
import json



def instadownLoader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "7f3e694761mshec679b5f0557f9cp142cb2jsn59b13828e70e",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    rest=json.loads(response.text)
    if "error" in rest:
        return "Bad request"
    else:
        dict={}
        if rest["Type"]=="Post-Image":
            dict["type"]="image"
            dict["media"]=rest["media"]
            return dict
        elif rest["Type"]=="Post-Video":
            dict["type"]="video"
            dict["media"]=rest["media"]
            return dict
        elif rest["Type"]=="Carousel":
            dict["type"]="carousel"
            dict["media"]=rest["media"]
            return dict
        else:
            return "Bad Request"
        
        