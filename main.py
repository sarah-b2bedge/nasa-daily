import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")
RESPONSE_TITLE = os.getenv("RESPONSE_TITLE")
RESPONSE_VIDEO_TYPE = os.getenv("RESPONSE_VIDEO_TYPE")
RESPONSE_URL = os.getenv("RESPONSE_URL")
RESPONSE_EXPLANATION = os.getenv("RESPONSE_EXPLANATION")
RESPONSE_MEDIA_TYPE = os.getenv("RESPONSE_MEDIA_TYPE")

# Prepare API key and API url
url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"

# Get the request data as a dictionary
response = requests.get(url)
content = response.json()

# Extract the title, url, and explanation from the content and display them in the Streamlit app
st.title(content[RESPONSE_TITLE])
if content[RESPONSE_MEDIA_TYPE] == RESPONSE_VIDEO_TYPE:
    st.video(content[RESPONSE_URL])
else:
    st.image(content[RESPONSE_URL])
st.text(content[RESPONSE_EXPLANATION])