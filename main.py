import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Prepare API key and API ur
NASA_API_KEY = os.getenv("NASA_API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"

# Get the request data as a dictionary
response = requests.get(url)
content = response.json()

# Extract the title, url, and explanation from the content and display them in the Streamlit app
st.title(content["title"])
if content["media_type"] == "video":
    st.video(content["url"])
else:
    st.image(content["url"])
st.text(content["explanation"])