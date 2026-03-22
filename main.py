import streamlit as st
import requests

# Prepare API key and API ur
api_key = "hqGbT3TOzsGWXeYmS7znqVfsYXz9gzH79ifcgqtk"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Get the request data as a dictionary
response = requests.get(url)
content = response.json()

# Extract the title, url, and explanation from the content and display them in the Streamlit app
st.title(content["title"])
st.video(content["url"])
st.text(content["explanation"])