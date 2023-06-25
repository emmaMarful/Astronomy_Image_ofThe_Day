import PIL
import streamlit as web_ui
import requests


header = "Astronomy Picture Of the Day"
web_ui.title(header.title())

# nasa api key
apiKey = "ma4c1m3W5TFYAIyypmgkDbAwLLrb8aHbwWyOgNsQ"

# url to astronomy picture of the day
url ="https://api.nasa.gov/planetary/apod?" \
     f"api_key={apiKey}"

# request data from api
response = requests.get(url=url)

# api data stored
strApiData = response.json()

# display title of astronomy picture of the day on webpage
web_ui.header(strApiData["title"])


# extract apod image
img_url = strApiData["url"]

try:
    # create a jpg to save apod
    crt_img = "image.jpg"
    extract_img = requests.get(img_url)
    with open(crt_img, "wb") as imageSave:
        imageSave.write(extract_img.content)

    # display extracted web image to the web
    web_ui.image("image.jpg")
except PIL.UnidentifiedImageError:
    vid = "https://www.youtube.com/embed/YEXuGgRCyS0?rel=0"
    web_ui.video(vid)


date = f"Date: {strApiData['date']}"
web_ui.write(date)

# display explation of picture of the day
desc =strApiData["explanation"]
web_ui.write(desc)
